import json
from pathlib import Path
from datetime import datetime
def save(r,output="reports"):
 d=Path(output);d.mkdir(parents=True,exist_ok=True);b=d/("flexscan_"+datetime.now().strftime("%Y%m%d_%H%M%S_%f"))
 j=b.with_suffix(".json");t=b.with_suffix(".txt");j.write_text(json.dumps(r.to_dict(),indent=2,ensure_ascii=False),encoding="utf8")
 lines=[f"FlexTools Report\nTarget: {r.target}\nMode: {r.mode}\n"]
 for p in r.parameters:
  lines.append(f"\nParameter: {p.name}\nSeverity: {p.severity}\nConfidence: {p.confidence}/100")
  for s in p.signals:lines.append(f"  {s.name}: {'POSITIVE' if s.positive else 'negative'}\n    " + "\n    ".join(s.evidence))
 t.write_text("\n".join(lines),encoding="utf8");return str(j),str(t)
