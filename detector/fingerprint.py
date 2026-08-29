from core.config import ERROR_MARKERS
def classify(signals):
 t=" ".join(" ".join(s.evidence) for s in signals).lower();return [f for f,m in ERROR_MARKERS.items() if any(x in t for x in m)] or ["unknown"]
