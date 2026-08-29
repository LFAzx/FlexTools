from core.models import Signal
def run(c,u,p,n,b):
 q=dict(p);q[n]="__FLEX_STATUS_TEST__"
 try:
  r,_=c.get(u,q);pos=r.status_code>=500 and b["status"]<500
  return Signal("status_anomaly",pos,15 if pos else 0,[f"baseline={b['status']}",f"response={r.status_code}"])
 except Exception as e:return Signal("status_anomaly",False,0,[str(e)])
