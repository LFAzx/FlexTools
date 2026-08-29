from core.baseline import collect
from core.config import PROFILES
from core.models import ParameterResult,TargetResult
from core.scoring import calculate,severity
from scanner.url_parser import parse
from detector.error_based import run as error
from detector.boolean_based import run as boolean
from detector.length_analysis import run as length
from detector.status_analysis import run as status
from detector.timing_analysis import run as timing
from detector.fingerprint import classify
def scan_target(c,target,mode="soft"):
 prof=PROFILES[mode];out=TargetResult(target,mode)
 try:
  u,p=parse(target)
  if not p:out.errors.append("No URL query parameters. Run discover first.");return out
  b=collect(c,u,p,prof["baseline_samples"]);out.meta["baseline"]={k:v for k,v in b.items() if k!="texts"}
  allsig=[]
  for n in p:
   sig=[error(c,u,p,n,b),boolean(c,u,p,n,prof["similarity_threshold"]),length(c,u,p,n,b),status(c,u,p,n,b),timing(c,u,p,n,b,prof["timing_samples"])]
   allsig+=sig;score=calculate(sig)
   if score:out.parameters.append(ParameterResult(n,"GET",score,severity(score),sig))
  out.meta["dbms_fingerprint"]=classify(allsig)
 except Exception as e:out.errors.append(str(e))
 return out
