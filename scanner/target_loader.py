def load(url=None,url_file=None):
 x=[url.strip()] if url else []
 if url_file:
  with open(url_file,encoding="utf8") as f:x += [z.strip() for z in f if z.strip() and not z.startswith("#")]
 return list(dict.fromkeys(x))
