#!/usr/bin/env python3
"""Mutation regressions for the control checker; no network or theorem tests."""
import json
import hashlib
from pathlib import Path
import shutil
import tempfile
import unittest

from check_control import ROOT, CONTRACT_FIELDS, digest_json, validate, write_views


class ControlRegression(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / 'docs', self.root / 'docs')
        shutil.copytree(ROOT / 'experiments', self.root / 'experiments')
        shutil.copytree(ROOT / '.github', self.root / '.github')
        for name in ('README.md', 'AGENTS.md', 'LICENSE'):
            shutil.copy2(ROOT / name, self.root / name)

    def tearDown(self):
        self.temp.cleanup()

    def edit(self, path, old, new):
        p = self.root / path
        text = p.read_text(encoding='utf-8')
        self.assertIn(old, text)
        p.write_text(text.replace(old, new, 1), encoding='utf-8')

    def state_edit(self, edit, regenerate=False):
        p = self.root / 'docs/control-state.json'
        state = json.loads(p.read_text(encoding='utf-8'))
        edit(state)
        p.write_text(json.dumps(state), encoding='utf-8')
        if regenerate:
            write_views(self.root, state)

    def detects(self, fragment):
        failures = validate(self.root)
        self.assertTrue(any(fragment in f for f in failures), failures)

    def gate_fixture(self):
        """Synthetic record-format fixture, explicitly not mathematical evidence."""
        # III.14 is now a real registered theorem. Use the next unassigned number
        # only inside the temporary test tree so the fixture cannot collide with
        # the production control state or create a real III.15 candidate.
        unit_path = 'docs/principia-v3-15-fixture.md'
        review_path = 'docs/source-review-fixture.json'
        gate_path = 'docs/source-gate-fixture.json'
        (self.root / unit_path).write_text('# Synthetic III.15 fixture\n', encoding='utf-8')
        sha = lambda path: hashlib.sha256((self.root / path).read_bytes()).hexdigest()
        contract = {key: 'Test-only ' + key for key in CONTRACT_FIELDS}
        sources = [{'url': 'https://example.org/test-only', 'locator': 'fixture §1', 'supports': ['claim']}]
        review = {'schema': 1, 'kind': 'SOURCE_CONTRACT_REVIEW', 'unit_id': 'III.15',
                  'task_id': 'P9-I', 'unit_sha256': sha(unit_path),
                  'contract_sha256': digest_json(contract), 'sources_sha256': digest_json(sources),
                  'verdict': 'PASS', 'reviewer': 'synthetic test',
                  'checks': {key: True for key in CONTRACT_FIELDS}, 'scope': 'Format test only; no theorem review.'}
        (self.root / review_path).write_text(json.dumps(review), encoding='utf-8')
        gate = {'schema': 1, 'kind': 'SOURCE_CONTRACT_GATE', 'unit_id': 'III.15', 'task_id': 'P9-I',
                'unit': {'path': unit_path, 'sha256': sha(unit_path)},
                'evidence': {'path': review_path, 'sha256': sha(review_path)},
                'contract': contract, 'sources': sources}
        (self.root / gate_path).write_text(json.dumps(gate), encoding='utf-8')

        def edit(state):
            state['units'].append({'id': 'III.15', 'state': 'CONDITIONAL_PASS',
                                   'path': unit_path, 'evidence': review_path})
            state['gates']['III.15'] = {'state': 'PASS', 'task_id': 'P9-I', 'path': gate_path}
        self.state_edit(edit, regenerate=True)
        return gate_path, gate

    def gate_edit(self, edit):
        path, gate = self.gate_fixture()
        edit(gate)
        (self.root / path).write_text(json.dumps(gate), encoding='utf-8')

    def test_clean(self):
        self.assertEqual(validate(self.root), [])

    def test_unknown_unit_state_survives_regeneration_but_is_rejected(self):
        self.state_edit(lambda s: s['units'][0].update(state='PSSA'), regenerate=True)
        self.detects('invalid unit state')

    def test_unknown_task_state(self):
        self.state_edit(lambda s: s['tasks'][-1].update(state='PSSA'), regenerate=True)
        self.detects('invalid task state')

    def test_unknown_gate_state(self):
        self.state_edit(lambda s: s['gates']['III.13'].update(state='PSSA'))
        self.detects('invalid gate state')

    def test_unknown_schema(self):
        self.state_edit(lambda s: s.update(schema=99))
        self.detects('unsupported control schema')

    def test_valid_typed_gate_format(self):
        self.gate_fixture()
        self.assertEqual(validate(self.root), [])

    def test_readme_cannot_pass_as_source_gate(self):
        self.gate_fixture()
        self.state_edit(lambda s: s['gates']['III.15'].update(path='README.md'))
        self.detects('invalid typed gate')

    def test_gate_of_another_task(self):
        self.gate_edit(lambda g: g.update(task_id='TRAFFIC-OBSERVATION'))
        self.detects('wrong target task')

    def test_gate_of_another_unit(self):
        self.gate_edit(lambda g: g.update(unit_id='III.12'))
        self.detects('wrong target unit')

    def test_edited_unit_invalidates_review(self):
        _, gate = self.gate_fixture()
        (self.root / gate['unit']['path']).write_text('Changed theorem', encoding='utf-8')
        self.detects('artifact digest mismatch')

    def test_rehashed_unit_still_needs_new_review(self):
        path, gate = self.gate_fixture()
        (self.root / gate['unit']['path']).write_text('Changed theorem', encoding='utf-8')
        gate['unit']['sha256'] = hashlib.sha256(b'Changed theorem').hexdigest()
        (self.root / path).write_text(json.dumps(gate), encoding='utf-8')
        self.detects('reviewed unit digest mismatch')

    def test_edited_contract_invalidates_review(self):
        self.gate_edit(lambda g: g['contract'].update(conditions='Removed important hypothesis'))
        self.detects('reviewed contract digest mismatch')

    def test_missing_source_locator(self):
        self.gate_edit(lambda g: g['sources'][0].pop('locator'))
        self.detects('invalid source locator')

    def test_unrelated_evidence_with_correct_hash_is_rejected(self):
        def change(gate):
            path = 'docs/principia-v3-p9h-composition-crosscheck-01.md'
            gate['evidence'] = {'path': path, 'sha256': hashlib.sha256((self.root / path).read_bytes()).hexdigest()}
        self.gate_edit(change)
        self.detects('artifact belongs to a different unit/evidence')

    def test_artifact_cannot_escape_repository(self):
        self.gate_edit(lambda g: g['unit'].update(path=str(ROOT / 'README.md')))
        self.detects('missing/local artifact path')

    def test_duplicate_current(self):
        (self.root / 'docs/duplicate.md').write_text('**Control role:** `claim-registry`', encoding='utf-8')
        self.detects('current role is not unique')

    def test_stale_readme(self):
        self.edit('README.md', '](docs/claim-registry.md)', '](docs/claim-registry-13.md)')
        self.detects('README points to a historical')

    def test_broken_link(self):
        self.edit('README.md', '](docs/core.md)', '](docs/absent.md)')
        self.detects('broken local link')

    def test_missing_claim(self):
        self.edit('docs/claim-registry.md', '## C67 —', '### C67 —')
        self.detects('C registry missing or duplicate')

    def test_duplicate_falsifier(self):
        with (self.root / 'docs/falsifier-registry.md').open('a', encoding='utf-8') as f:
            f.write('\n## F62 — duplicate\n')
        self.detects('F registry missing or duplicate')

    def test_latest_falsifier_snapshot_must_be_materialized(self):
        (self.root / 'docs/falsifier-registry-99.md').write_text(
            '# PSI — future falsifier snapshot\n\n## F99 — synthetic\n', encoding='utf-8')
        self.detects('falsifier-registry latest version not materialized')

    def test_recursive_registry(self):
        with (self.root / 'docs/claim-registry.md').open('a', encoding='utf-8') as f:
            f.write('\nRetain C01–C18 from the previous registry.\n')
        self.detects('registry is recursive')

    def test_withdrawn_version(self):
        self.edit('docs/claim-registry.md', '## C19-v3 —', '## C19-v2 —')
        self.detects('withdrawn C19 version')

    def test_wait_without_release(self):
        self.state_edit(lambda s: s['tasks'][0].pop('release'), regenerate=True)
        self.detects('lacks release')

    def test_stale_closed_frame_status(self):
        self.edit('docs/claim-registry.md', '**Current status:** `RESOLVED / SUPERSEDED BY C22–C23`',
                  '**Current status:** `CLOSED-FRAME=OPEN`')
        self.detects('C21 retains withdrawn OPEN status')

    def test_nonexecutable_selection(self):
        self.state_edit(lambda s: s['selection'].update(primary='TRAFFIC-INSTRUMENTATION'), regenerate=True)
        self.detects('primary task is not executable')

    def test_status_mismatch(self):
        self.edit('docs/theorem-map-v3.md', '| III.12 | CONDITIONAL_PASS |', '| III.12 | OPEN |')
        self.detects('V3 status mismatch')

    def test_work_map_mismatch(self):
        self.edit('docs/work-map.md', 'TRAFFIC-INSTRUMENTATION — WAIT', 'TRAFFIC-INSTRUMENTATION — PASS')
        self.detects('work map differs')

    def test_supersedes_cycle(self):
        self.state_edit(lambda s: s['supersedes'].update({'docs/claim-registry-01.md': ['docs/claim-registry.md']}))
        self.detects('supersedes cycle')

    def test_undeclared_unit(self):
        (self.root / 'docs/principia-v3-15-unlicensed.md').write_text('# III.15\n', encoding='utf-8')
        self.detects('unregistered theorem unit')

    def test_declared_unit_without_passed_gate(self):
        path = 'docs/principia-v3-15-unlicensed.md'
        (self.root / path).write_text('# III.15\n', encoding='utf-8')
        self.state_edit(lambda s: s['units'].append({'id': 'III.15', 'state': 'PASS', 'path': path,
                        'evidence': 'docs/principia-v3-p9h-composition-crosscheck-01.md'}), regenerate=True)
        self.detects('unpassed source gate')


if __name__ == '__main__':
    unittest.main(verbosity=2)
