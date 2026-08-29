import re
from difflib import SequenceMatcher
def normalize(t):return re.sub(r"\s+"," ",re.sub(r"\b\d{3,}\b","<NUM>",t)).strip().lower()
def similarity(a,b):return SequenceMatcher(None,normalize(a),normalize(b)).ratio()
