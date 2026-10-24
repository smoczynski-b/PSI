"""Finite one-step M013 oracle. Exhaustive partitions; no model, network or core imports."""
from __future__ import annotations
import hashlib,itertools,json,time,datetime,sys
from collections import Counter,defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parent

class ContractError(ValueError):pass

def partitions(n):
 if n==0:
  yield ()
  return
 def grow(prefix):
  if len(prefix)==n:
   yield prefix
   return
  for label in range(max(prefix)+2):
   yield from grow(prefix+(label,))
 yield from grow((0,))

def tables(rows, *, actions=None, terminal_only=True, alphabet=None):
 if not isinstance(rows,list) or not 1<=len(rows)<=4:raise ContractError('OUT_OF_SCOPE_N')
 if not terminal_only:raise ContractError('OUT_OF_SCOPE_C4_NONTERMINAL_SUCCESSOR')
 if actions is not None and (len(actions)!=len(rows) or len(set(actions))!=1):
  raise ContractError('OUT_OF_SCOPE_C2_DIFFERENT_ACTION_OR_POLICY')
 result=[]
 for row in rows:
  pairs=list(row.items()) if isinstance(row,dict) else row
  if not isinstance(pairs,list):raise ContractError('INVALID_CONTRACT_TABLE')
  current={}
  for report,value in pairs:
   if not isinstance(report,str) or not report or type(value) is not int:raise ContractError('INVALID_MODEL_TYPE')
   if alphabet is not None and report not in alphabet:raise ContractError('INVALID_CONTRACT_NONPHYSICAL_REPORT')
   if report in current and current[report]!=value:raise ContractError('INVALID_MODEL_AMBIGUOUS_REPORT')
   current[report]=value
  if len(set(current.values()))<2:raise ContractError('INVALID_CONTRACT_RESOLVED_INITIAL_STATE')
  result.append(current)
 return result

def candidate(rows,labels,J):
 # ACT/STOP use separate code spaces; terminal codes preserve exact q.
 U={};signatures={}
 for i,row in enumerate(rows):
  code=labels[i];signature=frozenset(set(row)&J)
  if code in signatures and signatures[code]!=signature:return None
  signatures[code]=signature
  for report,value in row.items():
   key=(code,report);target=('STOP',value)
   if key in U and U[key]!=target:return None
   U[key]=target
 # Verify own coded successors on every actual transition, not ker inclusion.
 if any(U[(labels[i],report)]!=('STOP',value)
        for i,row in enumerate(rows) for report,value in row.items()):
  return None
 return U

def oracle(rows,J=frozenset()):
 rows=tables(rows);J=set(J);r=len({v for row in rows for v in row.values()})
 accepted=Counter();opt=None;best=len(rows)+1;checked=0
 for labels in partitions(len(rows)):
  checked+=1
  U=candidate(rows,labels,J)
  if U is None:continue
  k=1+max(labels);accepted[k]+=1
  if k<best:best=k;opt=(labels,U)
 assert opt is not None
 labels,U=opt
 return {'m':r+best,'k':best,'r':r,'partitions_checked':checked,
  'admissible_by_k':dict(sorted(accepted.items())),
  'optimal_partition':[[i+1 for i,label in enumerate(labels) if label==c] for c in range(best)],
  'own_update_witness':[{'code':code,'report':o,'terminal_value':v[1]} for (code,o),v in sorted(U.items())],
  'checked_contract':{'C1':'STOP(value)','C2':'ONE_FIXED_ACTION','C3':'OWN_CODE_UPDATE_EXPLICIT','C4':'ONE_STEP_TO_TERMINAL','preserved_reports':sorted(J)}}

def chromatic(n,edges):
 # Separate all-color-assignments oracle, independent of restricted-growth enumeration.
 if n==0:return 0
 for k in range(1,n+1):
  for colors in itertools.product(range(k),repeat=n):
   if all(colors[i]!=colors[j] for i,j in edges):return k
 raise AssertionError('NO_COLORING')

def graph_check(rows,J):
 edges={(i,j) for i in range(len(rows)) for j in range(i+1,len(rows))
        if any(rows[i][o]!=rows[j][o] for o in set(rows[i])&set(rows[j]))}
 full=edges|{(i,j) for i in range(len(rows)) for j in range(i+1,len(rows))
            if set(rows[i])&J!=set(rows[j])&J}
 layers=defaultdict(list)
 for i,row in enumerate(rows):layers[tuple(sorted(set(row)&J))].append(i)
 total=0
 for members in layers.values():
  relabel={old:new for new,old in enumerate(members)}
  local={(relabel[i],relabel[j]) for i,j in edges if i in relabel and j in relabel}
  total+=chromatic(len(members),local)
 return {'chromatic':chromatic(len(rows),full),'layer_chromatic_sum':total}

def pair(rows):
 rows=tables(rows)
 return {'C3':oracle(rows),'C3plus':oracle(rows,set().union(*map(set,rows)))}

def physical(n,kind,patterns=None):
 if kind=='xor':
  states=[(i,t) for i in range(1,n+1) for t in (0,1)]
  q={s:s[1] for s in states};old={s:('x' if (s[0]-1)^s[1]==0 else 'y') for s in states}
 elif kind=='reveal':
  states=[(i,t) for i in range(1,n+1) for t in (0,1)]
  q={s:s[1] for s in states};old={s:str(s[1]) for s in states}
 else:
  states=[(i,o) for i in range(1,n+1) for o in 'abc']
  q={(i,o):int(patterns[i-1]['abc'.index(o)]) for i,o in states}
  old={(i,o):o for i,o in states}
 beliefs=[[s for s in states if s[0]==i] for i in range(1,n+1)]
 new={s:str(s[0])+':'+old[s] for s in states}
 coarsen={value:value.split(':',1)[1] for value in new.values()}
 return states,beliefs,q,old,new,coarsen

def physical_check(states,beliefs,q,old,new,coarsen,*,q_after=None,beliefs_after=None):
 if q_after is not None and q_after!=q:raise ContractError('INVALID_REFINEMENT_CHANGED_Q')
 if beliefs_after is not None and beliefs_after!=beliefs:raise ContractError('INVALID_REFINEMENT_CHANGED_B')
 if set(states)!=set(q) or set(old)!=set(states) or set(new)!=set(states):raise ContractError('INVALID_REFINEMENT_CHANGED_S')
 witness=[]
 for s in states:
  if coarsen.get(new[s])!=old[s]:raise ContractError('INVALID_REFINEMENT_FACTORIZATION')
  witness.append({'state':list(s),'q':q[s],'old':old[s],'new':new[s],'coarsened':coarsen[new[s]]})
 def derive(observation):
  rows=[]
  for B in beliefs:
   rows.append([(observation[s],q[s]) for s in B])
  return tables(rows)
 return derive(old),derive(new),witness

def negative(name,expected,fn):
 try:fn()
 except ContractError as exc:
  assert expected in str(exc),(name,str(exc))
  return {'id':name,'status':'EXPECTED_REJECTION','reason':str(exc)}
 raise AssertionError('INVALID_INPUT_ACCEPTED:'+name)

def powerset(items):
 return [frozenset(c) for n in range(len(items)+1) for c in itertools.combinations(items,n)]

def run():
 started=time.perf_counter()
 assert [len(list(partitions(n))) for n in (1,2,3,4)]==[1,2,5,15]
 result={'packet01':{},'packet02':{},'negative_controls':[],'physical_checks':{}}
 fixtures=json.loads((ROOT/'INPUTS.json').read_text(encoding='utf8'))
 # No expected value is read until after the exhaustive oracle returns.
 for case in fixtures['packet01']:
  computed=pair(case['tables'])
  got=[computed['C3']['m'],computed['C3plus']['m']]
  computed['expected']=case['expected'];computed['status']='PASS' if got==case['expected'] else 'FAIL'
  result['packet01'][case['id']]=computed
  assert got==case['expected'],(case['id'],got,case['expected'])
 for name,n,kind,patterns,expected in [
  ('K1',2,'xor',None,[[4,4],[3,4]]),
  ('K2',4,'reveal',None,[[3,3],[3,6]]),
  ('K1_n4',4,'patterns',['001','010','100','110'],[[6,6],[3,6]])]:
  model=physical(n,kind,patterns);before,after,witness=physical_check(*model)
  pairs=[pair(before),pair(after)]
  got=[[p['C3']['m'],p['C3plus']['m']] for p in pairs]
  assert got==expected,(name,got)
  assert pairs[1]['C3']['m']<=pairs[0]['C3']['m']
  assert pairs[1]['C3plus']['m']>=pairs[0]['C3plus']['m']
  result['physical_checks'][name]={'status':'PASS','microstate_witness':witness,'before':pairs[0],'after':pairs[1]}
 # Delta=1 and single-table extension checks, independent of physical refinement.
 deltas={}
 for name in ('B2','B3','B4'):
  pre=result['packet01'][name+'_pre'];post=result['packet01'][name+'_post']
  delta=post['C3']['r']-pre['C3']['r']
  weak=post['C3']['m']-pre['C3']['m'];strong=post['C3plus']['m']-pre['C3plus']['m']
  assert delta<=weak<=delta+1 and delta-1<=strong<=delta+1
  originals={c['id']:c['tables'] for c in fixtures['packet01']}
  oldrows=originals[name+'_pre'];newrows=originals[name+'_post']
  changed=[i for i in range(len(oldrows)) if oldrows[i]!=newrows[i]]
  assert len(changed)==1
  j=changed[0];d=oldrows[j];e=newrows[j]
  assert set(d)<set(e) and len(set(e)-set(d))==1 and all(e[o]==v for o,v in d.items())
  n_d=sum(row==d for row in oldrows);n_e=sum(row==e for i,row in enumerate(oldrows) if i!=j)
  predicted=delta+int(n_e==0)-int(n_d==1)
  assert strong==predicted
  deltas[name]={'terminal_delta':delta,'C3_delta':weak,'C3plus_delta':strong,'T5_exact_prediction':predicted,'n_d':n_d,'n_e':n_e}
 assert deltas['B4']['terminal_delta']==1
 result['delta_checks']=deltas
 neg=result['negative_controls']
 neg.append(negative('resolved_initial','RESOLVED_INITIAL',lambda:tables([{'a':0}])))
 neg.append(negative('ambiguous_report','AMBIGUOUS_REPORT',lambda:tables([[('a',0),('a',1),('b',1)]])))
 neg.append(negative('different_actions','OUT_OF_SCOPE_C2',lambda:tables([{'a':0,'b':1}]*2,actions=['a','b'])))
 neg.append(negative('nonterminal_cycle','OUT_OF_SCOPE_C4',lambda:tables([{'a':0,'b':1}],terminal_only=False)))
 neg.append(negative('synthetic_BOT','NONPHYSICAL_REPORT',lambda:tables([{'a':0,'b':1,'BOT':0}],alphabet={'a','b'})))
 model=physical(2,'xor');states,B,q,old,new,c=model
 neg.append(negative('bad_factorization','FACTORIZATION',lambda:physical_check(states,B,q,old,new,{k:'bad' for k in c})))
 neg.append(negative('changed_q','CHANGED_Q',lambda:physical_check(*model,q_after={s:0 for s in states})))
 neg.append(negative('changed_B','CHANGED_B',lambda:physical_check(*model,beliefs_after=B[:1])))
 assert result['packet01']['B1']['C3']['m']==3 and result['packet01']['B1']['C3plus']['m']==4
 # Packet02 runs after packet01, within the same process and scope.
 for case in fixtures['packet02']:
  rows=tables(case['tables']);J=set(case['J']);got=oracle(rows,J)
  graph=graph_check(rows,J)
  assert got['k']==graph['chromatic']==graph['layer_chromatic_sum']
  assert got['m']==case['expected'],(case['id'],got)
  result['packet02'][case['id']]={'status':'PASS','oracle':got,'graph_comparison':graph}
 s2=tables(fixtures['families']['S2']);broken=oracle(s2)['m'];correct=oracle(s2,{'y'})['m']
 assert (broken,correct)==(4,6)
 result['packet02']['S4']={'status':'EXPECTED_REJECTIONS','controls':['resolved_initial','ambiguous_report','synthetic_BOT']}
 result['packet02']['S3']={'status':'REJECT_BROKEN_ORACLE','broken_m':broken,'correct_m':correct}
 meta={}
 for name,alphabet in [('S1',['x','z','y','t','w']),('S2',['x','z','y'])]:
  rows=tables(fixtures['families'][name]);sets=powerset(alphabet)
  values={J:oracle(rows,J) for J in sets}
  comparisons=0;one_step=0
  for J,base in values.items():
   graph=graph_check(rows,set(J));assert base['k']==graph['chromatic']==graph['layer_chromatic_sum']
   for K,newval in values.items():
    if J<K:
     comparisons+=1;assert base['k']<=newval['k']
     if len(K-J)==1:
      one_step+=1;assert newval['k']<=2*base['k']
  meta[name]={'status':'PASS','subsets':len(sets),'monotonic_pairs':comparisons,'one_report_edges':one_step,
             'results':[{'J':sorted(J),**v} for J,v in values.items()]}
 result['packet02']['S5']=meta
 result.update(status='PASS_SCOPED',scope='FINITE_ONE_STEP_N_LE_4_FALSIFICATION_ONLY',
  completed_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.perf_counter()-started,
  execution_order=['M013-01','M013-02'],additional_model_calls=0,
  general_theorem_certified=False,production_deployed=False,
  source_references=fixtures['sources'],code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
  source_snapshot_sha256=hashlib.sha256((ROOT/'SOURCES.json').read_bytes()).hexdigest(),
  input_sha256=hashlib.sha256((ROOT/'INPUTS.json').read_bytes()).hexdigest())
 (ROOT/'RECEIPT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8',newline='\n')
 print(json.dumps({'status':result['status'],'packet01_cases':len(result['packet01']),
  'physical_refinements':len(result['physical_checks']),'negative_controls':len(neg),
  'packet02_direct_cases':len(fixtures['packet02']),'S5_subsets':sum(v['subsets'] for v in meta.values()),
  'S5_monotonic_pairs':sum(v['monotonic_pairs'] for v in meta.values()),
  'S5_one_report_edges':sum(v['one_report_edges'] for v in meta.values()),
  'elapsed_seconds':result['elapsed_seconds']},indent=2))

if __name__=='__main__':run()
