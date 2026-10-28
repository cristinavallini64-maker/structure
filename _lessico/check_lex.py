#!/usr/bin/env python3
# Controlli aggiuntivi sui file di lessico: python3 check_lex.py N
# 1 audit (blocco A)  2 doppioni con Esercitati/Cambridge/libro  3 esempi delle schede
# 4 coerenza schede <-> esercizi  5 prova di funzionamento (jsdom)  6 parole nascondibili
import re, sys, subprocess, importlib, json, os
N = int(sys.argv[1])
EX = {1:"past-narrative",2:"present-perfect-advanced",3:"verb-patterns",4:"past-perfect-relatives",5:"first-conditional",
      6:"second-conditional",7:"modals-advice",8:"modal-deduction",9:"passive-voice",10:"reported-speech"}[N]
F = f"lessico-u{N}.html"
ok = True
def toks(s):
    s=s.lower(); s=re.sub(r'_+',' ',s); s=re.sub(r"[^a-z0-9' ]",' ',s); return set(s.split())
def jac(a,b):
    A,B=toks(a),toks(b); return len(A&B)/len(A|B) if A and B else 0

r = subprocess.run(["python3","audit-grammar-quest.py",F],capture_output=True,text=True).stdout
print("\n".join(l for l in r.splitlines() if l.startswith("[") or l.startswith("ESITO") or l.startswith("        ")
                and not l.startswith("        nomi")))
if "TUTTO PASS" not in r: ok=False

L=open(F,encoding="utf-8").read(); LV=L[L.index('const LEVELS='):L.index('const SK=')]
items=[q.replace('___',a) for q,a in re.findall(r'q:"([^"]+)",hint:"[^"]*",a:"([^"]+)"',LV)]
P=open(EX+".html",encoding="utf-8").read()
pn=re.findall(r'(?:q|wrong|a|original):"((?:[^"\\]|\\.){12,})"',P[P.index('const LEVELS='):P.index('const SK=')])
C=open(f"cambridge-u{N}.html",encoding="utf-8").read()
ct=[z for t in re.findall(r'(?:text|prompt):`?"?([^`"]{12,})',C) for z in re.split(r'(?<=[.?!])\s+',t)]
lib=[l.strip() for l in open(f"libro-u{N}.txt",encoding="utf-8") if l.strip() and not l.startswith('#')] if os.path.exists(f"libro-u{N}.txt") else []
x=[(round(jac(a,b),2),a[:70],b[:70]) for a in items for b in pn+ct+lib if jac(a,b)>=0.35]
print(f"\n[{'PASS' if not x else 'FAIL'}] X1: frasi vicine (>=0.35) a {EX}.html / cambridge-u{N} / libro ({len(lib)} frasi): {len(x)}")
for t in sorted(x,reverse=True)[:15]: print("        ",t)
if x: ok=False

C2=importlib.import_module(f"content_u{N}"); S=C2.STUDY
ex=[row[2] for v in S.values() for row in v]
y=[(round(jac(e,o),2),e[:70],o[:70]) for e in ex for o in items+pn+ct+lib if jac(e,o)>=0.35]
y+=[(round(jac(a,b),2),a[:70],b[:70]) for i,a in enumerate(ex) for b in ex[i+1:] if jac(a,b)>=0.35]
print(f"[{'PASS' if not y else 'FAIL'}] X2: esempi delle schede vicini a esercizi/altri file/altre schede: {len(y)}")
for t in sorted(y,reverse=True)[:15]: print("        ",t)
if y: ok=False

study_ids=set(S); lev_ids={str(l['id']) for l in C2.LEVELS if l['type']=='study'}
bad=[r_ for v in S.values() for r_ in v if len(r_)<4 or not all(isinstance(z,str) and z.strip() for z in r_[:4])]
print(f"[{'PASS' if study_ids==lev_ids and not bad else 'FAIL'}] X3: schede per ogni livello di studio {sorted(study_ids)} vs {sorted(lev_ids)}; schede incomplete: {len(bad)} | schede totali: {sum(map(len,S.values()))}")
if study_ids!=lev_ids or bad: ok=False

js=r"""
const {JSDOM}=require('jsdom');const fs=require('fs');
const html=fs.readFileSync(process.argv[2],'utf8').replace(/<script src=[^>]*><\/script>/g,'');
const dom=new JSDOM(html,{runScripts:'dangerously',pretendToBeVisual:true,url:'https://x.test/'});
const w=dom.window;w.scrollTo=()=>{};let ok=0,ko=[],wrongAcc=0,errs=0,nokey=[];
w.addEventListener('error',e=>errs++);
const L=w.eval('LEVELS');
for(const lv of L){ for(const [i,ex] of lv.exercises.entries()){
  for(const ans of (ex.accept||[ex.a])){
    w.eval(`currentLevel=LEVELS.find(l=>String(l.id)==='${lv.id}');exQueue=[currentLevel.exercises[${i}]];exIdx=0;isRetry=false;retryQueue=[];okCount=0;badCount=0;renderExercise();`);
    w.document.getElementById('fillInput').value=ans; w.eval('checkExercise()');
    if(w.eval('okCount')===1) ok++; else ko.push([lv.id,ex.a,ans]);
  }
  w.eval(`exQueue=[currentLevel.exercises[${i}]];exIdx=0;okCount=0;badCount=0;renderExercise();`);
  w.document.getElementById('fillInput').value='xyz wrong'; w.eval('checkExercise()');
  if(w.eval('okCount')===1) wrongAcc++;
}}
for(const id of Object.keys(w.eval('STUDY'))){w.eval('openStudy("'+id+'")');
  w.document.querySelectorAll('.st-card').forEach(c=>{if(!c.querySelector('.st-ex .st-key'))nokey.push(c.querySelector('.st-word').textContent)});}
console.log(JSON.stringify({ok,ko:ko.slice(0,8),nko:ko.length,wrongAcc,errs,nokey}));
"""
open("_t.js","w").write(js)
o=json.loads(subprocess.run(["node","_t.js",F],capture_output=True,text=True).stdout.strip().splitlines()[-1])
good = o["nko"]==0 and o["wrongAcc"]==0 and o["errs"]==0
print(f"[{'PASS' if good else 'FAIL'}] X4: risposte accettate {o['ok']}, rifiutate per errore {o['nko']} {o['ko']}, sbagliate accettate {o['wrongAcc']}, errori JS {o['errs']}")
print(f"[{'PASS' if not o['nokey'] else 'FAIL'}] X5: schede in cui la parola non si copre nell'esempio: {o['nokey']}")
if not good or o['nokey']: ok=False
print("\nESITO CONTROLLI LESSICO:", "TUTTO PASS" if ok else "DA SISTEMARE")
