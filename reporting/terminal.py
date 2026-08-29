from core.colors import *
def show_discovery(t,d):
 print("\n"+bold(cyan("╔══ PARAMETER DISCOVERY ═══════════════════════════════════════╗")))
 print(f"{bold('TARGET')}  {magenta(t)}")
 total=sum(len(x) for x in d.values()); print(f"{bold('FOUND')}   {green(str(total))} candidate parameters")
 for k,v in d.items():
  print("\n"+bold(blue("["+k+"]")))
  if v:
   for x in v: print("  "+cyan("•")+" "+yellow(x))
  else: print("  "+dim("No candidates found"))

def show(r):
 print("\n"+bold(cyan("╔══ FLEXTOOLS ANALYSIS RESULT ═════════════════════════════════╗")))
 print(f"{bold('TARGET')}  {magenta(r.target)}")
 print(f"{bold('MODE')}    "+(green(r.mode.upper()) if r.mode=="soft" else yellow(r.mode.upper())))
 for e in r.errors: print(red("[!] ") + e)
 if r.meta.get("baseline"):
  b=r.meta["baseline"];print("\n"+bold(blue("BASELINE")))
  print(f"  status={b['status']}  length={b['length_avg']:.1f}  time={b['time_avg']:.3f}s")
 if not r.parameters: print("\n"+yellow("[-] No suspicious parameters flagged."))
 for p in r.parameters:
  sev={"HIGH":red,"MEDIUM":yellow,"LOW":cyan,"INFO":dim}.get(p.severity,dim)
  print("\n"+bold(green("[+] PARAMETER: ")) + yellow(p.name) + " | " + sev(p.severity) + f" | {p.confidence}/100")
  for s in p.signals:
   marker=green("[POSITIVE]") if s.positive else dim("[negative]")
   print(f"    {marker} {bold(s.name)}")
   for e in s.evidence: print("        "+dim("└─")+" "+e)
 print("\n"+bold(blue("DBMS FINGERPRINT"))+"  "+cyan(", ".join(r.meta.get("dbms_fingerprint",[]))))
 print(bold(cyan("╚══════════════════════════════════════════════════════════════╝")))
