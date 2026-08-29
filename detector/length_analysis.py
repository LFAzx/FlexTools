from core.models import Signal
def run(c,u,p,n,b):
 q=dict(p);q[n]="__FLEX_LENGTH_TEST__"
 try:
  r,_=c.get(u,q);base=max(1,b["length_avg"]);d=abs(len(r.text)-base)/base;pos=d>=.40
  return Signal("length_anomaly",pos,15 if pos else 0,[f"baseline_avg={base:.1f}",f"response={len(r.text)}",f"delta={d:.2%}"],{"delta":d})
 except Exception as e:return Signal("length_anomaly",False,0,[str(e)])
