from core.models import Signal
from core.config import ERROR_MARKERS
def run(c,u,p,n,b):
 q=dict(p);q[n]="__FLEX_PROBE__'"
 try:
  r,_=c.get(u,q);txt=r.text.lower();base=" ".join(b["texts"]).lower();hits=[]
  for fam,marks in ERROR_MARKERS.items():
   hits += [f"{fam}:{m}" for m in marks if m in txt and m not in base]
  return Signal("error_based",bool(hits),40 if hits else 0,hits,{"status":r.status_code})
 except Exception as e:return Signal("error_based",False,0,[str(e)])
