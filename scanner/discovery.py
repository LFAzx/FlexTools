import re
from urllib.parse import urljoin,urlsplit,parse_qsl
from scanner.url_parser import parse
def discover(c,target):
 clean,params=parse(target);found={"GET":set(params),"FORM":set(),"LINK":set()}
 try:
  r,_=c.get(target)
  for n in re.findall(r'<(?:input|select|textarea)[^>]*\bname=["\']([^"\']+)["\']',r.text,re.I):found["FORM"].add(n)
  for h in re.findall(r'href=["\']([^"\']+)["\']',r.text,re.I):
   for k,_ in parse_qsl(urlsplit(urljoin(target,h)).query,keep_blank_values=True):found["LINK"].add(k)
 except Exception:pass
 return {k:sorted(v) for k,v in found.items()}
