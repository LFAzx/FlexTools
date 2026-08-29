import requests,time
class HTTPClient:
 def __init__(self,timeout=10):
  self.timeout=timeout;self.session=requests.Session();self.session.headers.update({"User-Agent":"FlexTools/2.0 Authorized Security Scanner"})
 def get(self,url,params=None):
  s=time.perf_counter();r=self.session.get(url,params=params,timeout=self.timeout,allow_redirects=True);return r,time.perf_counter()-s
