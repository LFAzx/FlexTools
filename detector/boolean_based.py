from core.models import Signal
from core.normalizer import similarity
def run(c,u,p,n,th):
 a,b=dict(p),dict(p);a[n]="1";b[n]="0"
 try:
  r1,_=c.get(u,a);r2,_=c.get(u,b);sim=similarity(r1.text,r2.text);pos=r1.status_code!=r2.status_code or sim<th
  return Signal("boolean_differential",pos,30 if pos else 0,[f"similarity={sim:.3f}",f"status={r1.status_code}/{r2.status_code}"],{"similarity":sim})
 except Exception as e:return Signal("boolean_differential",False,0,[str(e)])
