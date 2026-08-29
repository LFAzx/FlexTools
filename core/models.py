from dataclasses import dataclass,field,asdict
from typing import List,Dict,Any
@dataclass
class Signal:
 name:str; positive:bool; score:int; evidence:List[str]=field(default_factory=list); metrics:Dict[str,Any]=field(default_factory=dict)
@dataclass
class ParameterResult:
 name:str; location:str; confidence:int; severity:str; signals:List[Signal]=field(default_factory=list)
@dataclass
class TargetResult:
 target:str; mode:str; parameters:List[ParameterResult]=field(default_factory=list); errors:List[str]=field(default_factory=list); meta:Dict[str,Any]=field(default_factory=dict)
 def to_dict(self): return asdict(self)
