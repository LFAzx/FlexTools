import sys,argparse
from concurrent.futures import ThreadPoolExecutor,as_completed
from core.http_client import HTTPClient
from core.config import PROFILES
from scanner.target_loader import load
from scanner.discovery import discover
from scanner.engine import scan_target
from reporting.terminal import show,show_discovery
from reporting.report_manager import save
from reporting.colored_help import root_help,command_help,header

def parser():
 p=argparse.ArgumentParser(prog="FlexTools",add_help=False)
 p.add_argument("-h","--help",action="store_true")
 sub=p.add_subparsers(dest="command")
 for name in ("detector","scan"):
  x=sub.add_parser(name,add_help=False)
  x.add_argument("-h","--help",action="store_true")
  x.add_argument("--url");x.add_argument("--url-file")
  x.add_argument("--mode",choices=PROFILES,default="soft")
  x.add_argument("--threads",type=int);x.add_argument("--timeout",type=int,default=10);x.add_argument("--output",default="reports")
 d=sub.add_parser("discover",add_help=False);d.add_argument("-h","--help",action="store_true");d.add_argument("--url");d.add_argument("--timeout",type=int,default=10)
 r=sub.add_parser("report",add_help=False);r.add_argument("-h","--help",action="store_true");r.add_argument("--list",action="store_true");r.add_argument("--dir",default="reports")
 return p

def main():
 p=parser()
 if len(sys.argv)==1: root_help();return
 a=p.parse_args()
 if a.command is None or a.help: root_help();return
 if getattr(a,"help",False): command_help(a.command);return
 if a.command=="discover":
  if not a.url: print("discover requires --url");return
  show_discovery(a.url,discover(HTTPClient(a.timeout),a.url));return
 if a.command=="report":
  if not a.list: command_help("report");return
  from pathlib import Path
  fs=sorted(Path(a.dir).glob("*"))
  print(header());print("\nREPORT DIRECTORY:",a.dir)
  if not fs: print("[-] No reports found")
  for f in fs: print("  •",f)
  return
 targets=load(a.url,a.url_file)
 if not targets: print(f"{a.command} requires --url or --url-file");return
 if a.command=="detector" and len(targets)!=1: print("detector accepts exactly one target");return
 c=HTTPClient(a.timeout);workers=1 if a.command=="detector" else (a.threads or PROFILES[a.mode]["threads"])
 print(header());print()
 with ThreadPoolExecutor(max_workers=max(1,workers)) as ex:
  for f in as_completed([ex.submit(scan_target,c,t,a.mode) for t in targets]):
   result=f.result();show(result);paths=save(result,a.output)
   print("\n[+] Reports saved:")
   for path in paths: print("    "+path)
if __name__=="__main__":main()
