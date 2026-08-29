def severity(s):return "HIGH" if s>=80 else "MEDIUM" if s>=55 else "LOW" if s>=30 else "INFO"
def calculate(signals):return min(100,sum(x.score for x in signals if x.positive))
