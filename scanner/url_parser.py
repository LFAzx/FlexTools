from urllib.parse import urlsplit,parse_qsl,urlunsplit
def parse(url):
 p=urlsplit(url);return urlunsplit((p.scheme,p.netloc,p.path,"",p.fragment)),dict(parse_qsl(p.query,keep_blank_values=True))
