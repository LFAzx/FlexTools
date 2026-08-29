import statistics
from core.models import Signal
def run(c,u,p,n,b,samples=3):
 ts=[]
 try:
  for v in ("1","2","3","4","5")[:samples]:
   q=dict(p);q[n]=v;_,t=c.get(u,q);ts.append(t)
  avg=statistics.mean(ts);spread=max(ts)-min(ts) if len(ts)>1 else 0;pos=avg>max(b["time_avg"]*3,b["time_avg"]+2) and spread<1
  return Signal("timing_anomaly",pos,10 if pos else 0,[f"baseline={b['time_avg']:.3f}s",f"avg={avg:.3f}s",f"spread={spread:.3f}s"])
 except Exception as e:return Signal("timing_anomaly",False,0,[str(e)])
