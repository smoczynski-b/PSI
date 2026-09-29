#!/usr/bin/env python3
"""Mutation regressions for the control checker; no network or theorem tests."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from check_control import ROOT, validate, write_views


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

    def test_clean(self):
        self.assertEqual(validate(self.root), [])

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
        (self.root / 'docs/principia-v3-13-unlicensed.md').write_text('# III.13\n', encoding='utf-8')
        self.detects('unregistered theorem unit')

    def test_declared_unit_without_passed_gate(self):
        path = 'docs/principia-v3-13-unlicensed.md'
        (self.root / path).write_text('# III.13\n', encoding='utf-8')
        self.state_edit(lambda s: s['units'].append({'id': 'III.13', 'state': 'PASS', 'path': path,
                        'evidence': 'docs/principia-v3-p9h-composition-crosscheck-01.md'}), regenerate=True)
        self.detects('unpassed source gate')


if __name__ == '__main__':
    unittest.main(verbosity=2)
