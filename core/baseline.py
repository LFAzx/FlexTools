import statistics
def collect(c,u,p,samples=3):
 rows=[]
 for _ in range(samples):
  r,t=c.get(u,p);rows.append((r.status_code,len(r.text),t,r.text))
 return {"status":statistics.mode([x[0] for x in rows]),"length_avg":statistics.mean([x[1] for x in rows]),"time_avg":statistics.mean([x[2] for x in rows]),"texts":[x[3] for x in rows]}
