
# This is an automatically generated file.
from copy import deepcopy
import math
from math import nan
import json
try:
    import pandas as pd
except:
    print('Warning: "pandas" package was not found.')

def float_equal(a:float|None, b:float|None) -> bool:
    if a is None and b is None: return True
    if a is None and b is not None: return False
    if b is None and a is not None: return False
    if math.isnan(a) and math.isnan(b): return True
    eps = 1e-9
    ab_diff = abs(a-b)
    if ab_diff<eps: return True
    ab_ratio = ab_diff/(abs(a/2 + b/2) + eps)
    if ab_ratio<eps: return True
    return False


# Forward declaration
class Error: pass
class Error:

    
    def __init__ (
        self,
        message:str|None = None,
        details:str|None = None,
        code:int|None = None,
        errors:list[Error]|None = None
    ):
        self.message : str|None = message
        self.details : str|None = details
        self.code : int|None = code
        self.errors : list[Error]|None = deepcopy(errors)
        pass

    def __eq__ (self, other):
        if self.message != other.message: return False
        if self.details != other.details: return False
        if self.code != other.code: return False
        if self.errors != other.errors: return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return Error_to_json_string(self)
def Error_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Error()
    Error_from_json(j,obj)
    return obj

def Error_to_json_string (self:Error):
    j = {}
    Error_to_json(j,self)
    return json.dumps(j)
def Error_from_json (j:dict, obj:Error):
    assert isinstance(obj,Error)
    if j.get("message",None) is not None:
        obj.message = j["message"]
    if j.get("details",None) is not None:
        obj.details = j["details"]
    if j.get("code",None) is not None:
        obj.code = j["code"]
    if j.get("errors",None) is not None:
        obj.errors = []
        for item in j["errors"]:
            v = Error()
            Error_from_json(item,v)
            obj.errors.append(v)
def Error_to_json(j:dict, obj:Error):
    if obj.message is not None:
        j["message"] = obj.message
    if obj.details is not None:
        j["details"] = obj.details
    if obj.code is not None:
        j["code"] = obj.code
    if obj.errors is not None:
        j["errors"] = []
        for item in obj.errors:
            jj = {}
            Error_to_json(jj,item)
            j["errors"].append(jj)


# Forward declaration
class UpdaterDoc: pass
class UpdaterDoc:

    
    def __init__ (
        self,
        name:str = "",
        title:str = "",
        doc_md:str = "",
        start:str = "",
        nargs_min:int = -88,
        nrefs_min:int = -88
    ):
        self.name : str = name
        self.title : str = title
        self.doc_md : str = doc_md
        self.start : str = start
        self.nargs_min : int = nargs_min
        self.nrefs_min : int = nrefs_min
        pass

    def __eq__ (self, other):
        if self.name != other.name: return False
        if self.title != other.title: return False
        if self.doc_md != other.doc_md: return False
        if self.start != other.start: return False
        if self.nargs_min != other.nargs_min: return False
        if self.nrefs_min != other.nrefs_min: return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return UpdaterDoc_to_json_string(self)
def UpdaterDoc_from_json_string (jstr):
    j = json.loads(jstr)
    obj = UpdaterDoc()
    UpdaterDoc_from_json(j,obj)
    return obj

def UpdaterDoc_to_json_string (self:UpdaterDoc):
    j = {}
    UpdaterDoc_to_json(j,self)
    return json.dumps(j)
def UpdaterDoc_from_json (j:dict, obj:UpdaterDoc):
    assert isinstance(obj,UpdaterDoc)
    obj.name = j["name"]
    obj.title = j["title"]
    obj.doc_md = j["doc_md"]
    obj.start = j["start"]
    obj.nargs_min = j["nargs_min"]
    obj.nrefs_min = j["nrefs_min"]
def UpdaterDoc_to_json(j:dict, obj:UpdaterDoc):
    j["name"] = obj.name
    j["title"] = obj.title
    j["doc_md"] = obj.doc_md
    j["start"] = obj.start
    j["nargs_min"] = obj.nargs_min
    j["nrefs_min"] = obj.nrefs_min


# Forward declaration
class UpdaterDto: pass
class UpdaterDto:

    
    def __init__ (
        self,
        name:str = "",
        refs:list[int]|None = None,
        args:list[float]|None = None,
        start:float|None = None
    ):
        self.name : str = name
        self.refs : list[int]|None = refs
        self.args : list[float]|None = args
        self.start : float|None = start
        pass

    def __eq__ (self, other):
        if self.name != other.name: return False
        if self.refs != other.refs: return False
        if self.args != other.args: return False
        if self.start != other.start: return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return UpdaterDto_to_json_string(self)
def UpdaterDto_from_json_string (jstr):
    j = json.loads(jstr)
    obj = UpdaterDto()
    UpdaterDto_from_json(j,obj)
    return obj

def UpdaterDto_to_json_string (self:UpdaterDto):
    j = {}
    UpdaterDto_to_json(j,self)
    return json.dumps(j)
def UpdaterDto_from_json (j:dict, obj:UpdaterDto):
    assert isinstance(obj,UpdaterDto)
    obj.name = j["name"]
    if j.get("refs",None) is not None:
        obj.refs = j["refs"]
    if j.get("args",None) is not None:
        obj.args = j["args"]
    if j.get("start",None) is not None:
        obj.start = j["start"]
def UpdaterDto_to_json(j:dict, obj:UpdaterDto):
    j["name"] = obj.name
    if obj.refs is not None:
        j["refs"] = obj.refs
    if obj.args is not None:
        j["args"] = obj.args
    if obj.start is not None:
        j["start"] = obj.start


# Forward declaration
class Updater: pass
class Updater (UpdaterDto):

    
    def __init__ (
        self,
        name:str = "",
        refs:list[int] = [],
        args:list[float] = [],
        start:float|None = None,
        title:str = ""
    ):
        super().__init__(
            name,
            refs,
            args,
            start,
        )
        self._equation : int = -88
        self._state : int = -88
        self.title : str = title
        pass

    def GetStateNumber (
        self,
    ):
        
        if self._state<0:
            raise Exception(f'Updater {self.name} has no state.')
        return self._state
        
        pass

    def GetEquationNumber (
        self,
    ):
        
        if self._equation<0:
            raise Exception(f'Updater {self.name} has no _equation.')
        return self._equation
        
        pass

    def HasState (
        self,
    ):
        
        return self.start is not None
        
        pass

    def GetStart (
        self,
    ):
        
        if self.start is None:
            raise ValueError()
        return self.start
        
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return Updater_to_json_string(self)
def Updater_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Updater()
    Updater_from_json(j,obj)
    return obj

def Updater_to_json_string (self:Updater):
    j = {}
    Updater_to_json(j,self)
    return json.dumps(j)
def Updater_from_json (j:dict, obj:Updater):
    assert isinstance(obj,Updater)
    UpdaterDto_from_json(j,obj)
def Updater_to_json(j:dict, obj:Updater):
    UpdaterDto_to_json(j,obj)


# Forward declaration
class IndependentGaussian: pass
class IndependentGaussian (Updater):

    
    def __init__ (
        self,
        refs:list[int] = [],
        title:str = ""
    ):
        super().__init__(
            "IndependentGaussian",
            refs,
            [],
            None,
            title,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return IndependentGaussian_to_json_string(self)
def IndependentGaussian_from_json_string (jstr):
    j = json.loads(jstr)
    obj = IndependentGaussian()
    IndependentGaussian_from_json(j,obj)
    return obj

def IndependentGaussian_to_json_string (self:IndependentGaussian):
    j = {}
    IndependentGaussian_to_json(j,self)
    return json.dumps(j)
def IndependentGaussian_from_json (j:dict, obj:IndependentGaussian):
    assert isinstance(obj,IndependentGaussian)
    Updater_from_json(j,obj)
def IndependentGaussian_to_json(j:dict, obj:IndependentGaussian):
    Updater_to_json(j,obj)


# Forward declaration
class CorrelatedGaussian: pass
class CorrelatedGaussian (Updater):

    
    def __init__ (
        self,
        correlation:float = nan,
        state1:int = -88,
        state2:int = -88,
        title:str = ""
    ):
        super().__init__(
            "CorrelatedGaussian",
            [state1,state2],
            [correlation],
            None,
            title,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return CorrelatedGaussian_to_json_string(self)
def CorrelatedGaussian_from_json_string (jstr):
    j = json.loads(jstr)
    obj = CorrelatedGaussian()
    CorrelatedGaussian_from_json(j,obj)
    return obj

def CorrelatedGaussian_to_json_string (self:CorrelatedGaussian):
    j = {}
    CorrelatedGaussian_to_json(j,self)
    return json.dumps(j)
def CorrelatedGaussian_from_json (j:dict, obj:CorrelatedGaussian):
    assert isinstance(obj,CorrelatedGaussian)
    Updater_from_json(j,obj)
def CorrelatedGaussian_to_json(j:dict, obj:CorrelatedGaussian):
    Updater_to_json(j,obj)


# Forward declaration
class BrownianMotion: pass
class BrownianMotion (Updater):

    
    def __init__ (
        self,
        start:float = nan,
        drift:float = nan,
        diffusion:float = nan,
        title:str = ""
    ):
        super().__init__(
            "BrownianMotion",
            [],
            [drift,diffusion],
            start,
            title,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return BrownianMotion_to_json_string(self)
def BrownianMotion_from_json_string (jstr):
    j = json.loads(jstr)
    obj = BrownianMotion()
    BrownianMotion_from_json(j,obj)
    return obj

def BrownianMotion_to_json_string (self:BrownianMotion):
    j = {}
    BrownianMotion_to_json(j,self)
    return json.dumps(j)
def BrownianMotion_from_json (j:dict, obj:BrownianMotion):
    assert isinstance(obj,BrownianMotion)
    Updater_from_json(j,obj)
def BrownianMotion_to_json(j:dict, obj:BrownianMotion):
    Updater_to_json(j,obj)


# Forward declaration
class BrownianMotionRef: pass
class BrownianMotionRef (Updater):

    
    def __init__ (
        self,
        start:float = nan,
        drift:int = -88,
        diffusion:int = -88,
        title:str = ""
    ):
        super().__init__(
            "BrownianMotion",
            [drift,diffusion],
            [],
            start,
            title,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return BrownianMotionRef_to_json_string(self)
def BrownianMotionRef_from_json_string (jstr):
    j = json.loads(jstr)
    obj = BrownianMotionRef()
    BrownianMotionRef_from_json(j,obj)
    return obj

def BrownianMotionRef_to_json_string (self:BrownianMotionRef):
    j = {}
    BrownianMotionRef_to_json(j,self)
    return json.dumps(j)
def BrownianMotionRef_from_json (j:dict, obj:BrownianMotionRef):
    assert isinstance(obj,BrownianMotionRef)
    Updater_from_json(j,obj)
def BrownianMotionRef_to_json(j:dict, obj:BrownianMotionRef):
    Updater_to_json(j,obj)


# Forward declaration
class GeometricalBrownianMotion: pass
class GeometricalBrownianMotion (Updater):

    
    def __init__ (
        self,
        start:float = nan,
        drift:float = nan,
        diffusion:float = nan,
        title:str = ""
    ):
        super().__init__(
            "GeometricalBrownianMotion",
            [],
            [drift,diffusion],
            start,
            title,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return GeometricalBrownianMotion_to_json_string(self)
def GeometricalBrownianMotion_from_json_string (jstr):
    j = json.loads(jstr)
    obj = GeometricalBrownianMotion()
    GeometricalBrownianMotion_from_json(j,obj)
    return obj

def GeometricalBrownianMotion_to_json_string (self:GeometricalBrownianMotion):
    j = {}
    GeometricalBrownianMotion_to_json(j,self)
    return json.dumps(j)
def GeometricalBrownianMotion_from_json (j:dict, obj:GeometricalBrownianMotion):
    assert isinstance(obj,GeometricalBrownianMotion)
    Updater_from_json(j,obj)
def GeometricalBrownianMotion_to_json(j:dict, obj:GeometricalBrownianMotion):
    Updater_to_json(j,obj)


# Forward declaration
class GeometricalBrownianMotionRef: pass
class GeometricalBrownianMotionRef (Updater):

    
    def __init__ (
        self,
        start:float = nan,
        drift:int = -88,
        diffusion:int = -88,
        title:str = ""
    ):
        super().__init__(
            "GeometricalBrownianMotion",
            [drift,diffusion],
            [],
            start,
            title,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return GeometricalBrownianMotionRef_to_json_string(self)
def GeometricalBrownianMotionRef_from_json_string (jstr):
    j = json.loads(jstr)
    obj = GeometricalBrownianMotionRef()
    GeometricalBrownianMotionRef_from_json(j,obj)
    return obj

def GeometricalBrownianMotionRef_to_json_string (self:GeometricalBrownianMotionRef):
    j = {}
    GeometricalBrownianMotionRef_to_json(j,self)
    return json.dumps(j)
def GeometricalBrownianMotionRef_from_json (j:dict, obj:GeometricalBrownianMotionRef):
    assert isinstance(obj,GeometricalBrownianMotionRef)
    Updater_from_json(j,obj)
def GeometricalBrownianMotionRef_to_json(j:dict, obj:GeometricalBrownianMotionRef):
    Updater_to_json(j,obj)


# Forward declaration
class ZeroCouponBond: pass
class ZeroCouponBond (Updater):

    
    def __init__ (
        self,
        underlying:int = -88,
        start:float = nan,
        title:str = ""
    ):
        super().__init__(
            "ZeroCouponBond",
            [underlying],
            [],
            start,
            title,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return ZeroCouponBond_to_json_string(self)
def ZeroCouponBond_from_json_string (jstr):
    j = json.loads(jstr)
    obj = ZeroCouponBond()
    ZeroCouponBond_from_json(j,obj)
    return obj

def ZeroCouponBond_to_json_string (self:ZeroCouponBond):
    j = {}
    ZeroCouponBond_to_json(j,self)
    return json.dumps(j)
def ZeroCouponBond_from_json (j:dict, obj:ZeroCouponBond):
    assert isinstance(obj,ZeroCouponBond)
    Updater_from_json(j,obj)
def ZeroCouponBond_to_json(j:dict, obj:ZeroCouponBond):
    Updater_to_json(j,obj)


# Forward declaration
class Option: pass
class Option (Updater):

    Call : int = 0
    Put : int = 1
    
    def __init__ (
        self,
        underlying:int = -88,
        strike:float = nan,
        call_put:int = -88,
        title:str = ""
    ):
        super().__init__(
            "Option",
            [underlying],
            [strike,call_put],
            0,
            title,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return Option_to_json_string(self)
def Option_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Option()
    Option_from_json(j,obj)
    return obj

def Option_to_json_string (self:Option):
    j = {}
    Option_to_json(j,self)
    return json.dumps(j)
def Option_from_json (j:dict, obj:Option):
    assert isinstance(obj,Option)
    Updater_from_json(j,obj)
def Option_to_json(j:dict, obj:Option):
    Updater_to_json(j,obj)


# Forward declaration
class Barrier: pass
class Barrier (Updater):

    DirectionUp : int = 1
    DirectionDown : int = -1
    DirectionAny : int = 0
    ActionSet : int = 0
    
    def __init__ (
        self,
        underlying:int = -88,
        start:float = nan,
        level:float = nan,
        direction:int = -88,
        action:int = -88,
        value:float = nan,
        title:str = ""
    ):
        super().__init__(
            "Barrier",
            [underlying],
            [level,value,direction,action],
            start,
            title,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return Barrier_to_json_string(self)
def Barrier_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Barrier()
    Barrier_from_json(j,obj)
    return obj

def Barrier_to_json_string (self:Barrier):
    j = {}
    Barrier_to_json(j,self)
    return json.dumps(j)
def Barrier_from_json (j:dict, obj:Barrier):
    assert isinstance(obj,Barrier)
    Updater_from_json(j,obj)
def Barrier_to_json(j:dict, obj:Barrier):
    Updater_to_json(j,obj)


# Forward declaration
class Linear1DInterpolation: pass
class Linear1DInterpolation (Updater):

    
    def __init__ (
        self,
        ref:int = -88,
        xmin:float = -1,
        xmax:float = 1,
        y:list[float] = [],
        title:str = ""
    ):
        super().__init__(
            "Linear1DInterpolation",
            [ref],
            [],
            0,
            title,
        )
        
        if len(y)<2:
            raise ValueError("Linear1DInterpolation: y-vector must have at least 2 elements: y(xmin), y(xmax)")
        self.args = [xmin,xmax] + y
        
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return Linear1DInterpolation_to_json_string(self)
def Linear1DInterpolation_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Linear1DInterpolation()
    Linear1DInterpolation_from_json(j,obj)
    return obj

def Linear1DInterpolation_to_json_string (self:Linear1DInterpolation):
    j = {}
    Linear1DInterpolation_to_json(j,self)
    return json.dumps(j)
def Linear1DInterpolation_from_json (j:dict, obj:Linear1DInterpolation):
    assert isinstance(obj,Linear1DInterpolation)
    Updater_from_json(j,obj)
def Linear1DInterpolation_to_json(j:dict, obj:Linear1DInterpolation):
    Updater_to_json(j,obj)


# Forward declaration
class Multiplication: pass
class Multiplication (Updater):

    
    def __init__ (
        self,
        refs:list[int] = [],
        factor:float = 1,
        title:str = ""
    ):
        super().__init__(
            "Multiplication",
            refs,
            [factor],
            0,
            title,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return Multiplication_to_json_string(self)
def Multiplication_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Multiplication()
    Multiplication_from_json(j,obj)
    return obj

def Multiplication_to_json_string (self:Multiplication):
    j = {}
    Multiplication_to_json(j,self)
    return json.dumps(j)
def Multiplication_from_json (j:dict, obj:Multiplication):
    assert isinstance(obj,Multiplication)
    Updater_from_json(j,obj)
def Multiplication_to_json(j:dict, obj:Multiplication):
    Updater_to_json(j,obj)


# Forward declaration
class HistogramAxis: pass
class HistogramAxis:

    
    def __init__ (
        self,
        _state:int = -88,
        _nbins:int = -88,
        _min:float = -88,
        _max:float = -88
    ):
        self.state : int = _state
        self.nbins : int = _nbins
        self.min : float = _min
        self.max : float = _max
        pass

    def __eq__ (self, other):
        if self.state != other.state: return False
        if self.nbins != other.nbins: return False
        if self.min != other.min: return False
        if self.max != other.max: return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return HistogramAxis_to_json_string(self)
def HistogramAxis_from_json_string (jstr):
    j = json.loads(jstr)
    obj = HistogramAxis()
    HistogramAxis_from_json(j,obj)
    return obj

def HistogramAxis_to_json_string (self:HistogramAxis):
    j = {}
    HistogramAxis_to_json(j,self)
    return json.dumps(j)
def HistogramAxis_from_json (j:dict, obj:HistogramAxis):
    assert isinstance(obj,HistogramAxis)
    obj.state = j["state"]
    obj.nbins = j["nbins"]
    obj.min = j["min"]
    obj.max = j["max"]
def HistogramAxis_to_json(j:dict, obj:HistogramAxis):
    j["state"] = obj.state
    j["nbins"] = obj.nbins
    j["min"] = obj.min
    j["max"] = obj.max


# Forward declaration
class Histogram: pass
class Histogram:

    
    def __init__ (
        self,
        x:HistogramAxis = HistogramAxis(),
        y:HistogramAxis|None = None
    ):
        self.x : HistogramAxis = deepcopy(x)
        self.y : HistogramAxis|None = deepcopy(y)
        pass

    def __eq__ (self, other):
        if self.x != other.x: return False
        if self.y != other.y: return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return Histogram_to_json_string(self)
def Histogram_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Histogram()
    Histogram_from_json(j,obj)
    return obj

def Histogram_to_json_string (self:Histogram):
    j = {}
    Histogram_to_json(j,self)
    return json.dumps(j)
def Histogram_from_json (j:dict, obj:Histogram):
    assert isinstance(obj,Histogram)
    HistogramAxis_from_json(j["x"],obj.x)
    if j.get("y",None) is not None:
        obj.y = HistogramAxis()
        HistogramAxis_from_json(j["y"],obj.y)
def Histogram_to_json(j:dict, obj:Histogram):
    jj = {}
    HistogramAxis_to_json(jj,obj.x)
    j["x"] = jj
    if obj.y is not None:
        jj = {}
        HistogramAxis_to_json(jj,obj.y)
        j["y"] = jj


# Forward declaration
class EvaluationPoint: pass
class EvaluationPoint:

    
    def __init__ (
        self,
        state:int = -88,
        time:float = nan,
        value:float|None = None,
        error:float|None = None,
        histograms:list[Histogram] = []
    ):
        self.state : int = state
        self.time : float = time
        self.value : float|None = value
        self.error : float|None = error
        self.histograms : list[Histogram] = deepcopy(histograms)
        pass

    def GetState (
        self,
    ):
        
        return self.state
        
        pass

    def GetTime (
        self,
    ):
        
        return self.time
        
        pass

    def GetValue (
        self,
    ):
        
        if self.value is None:
            raise ValueError()
        return self.value
        
        pass

    def GetError (
        self,
    ):
        
        if self.error is None:
            raise ValueError()
        return self.error
        
        pass

    def Add (
        self,
        histogram,
    ):
        
        self.histograms.append(histogram)
        return self
        
        pass

    def __eq__ (self, other):
        if self.state != other.state: return False
        if self.time != other.time: return False
        if self.value != other.value: return False
        if self.error != other.error: return False
        if self.histograms != other.histograms: return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return EvaluationPoint_to_json_string(self)
def EvaluationPoint_from_json_string (jstr):
    j = json.loads(jstr)
    obj = EvaluationPoint()
    EvaluationPoint_from_json(j,obj)
    return obj

def EvaluationPoint_to_json_string (self:EvaluationPoint):
    j = {}
    EvaluationPoint_to_json(j,self)
    return json.dumps(j)
def EvaluationPoint_from_json (j:dict, obj:EvaluationPoint):
    assert isinstance(obj,EvaluationPoint)
    obj.state = j["state"]
    obj.time = j["time"]
    if j.get("value",None) is not None:
        obj.value = j["value"]
    if j.get("error",None) is not None:
        obj.error = j["error"]
    obj.histograms = []
    for item in j["histograms"]:
        v = Histogram()
        Histogram_from_json(item,v)
        obj.histograms.append(v)
def EvaluationPoint_to_json(j:dict, obj:EvaluationPoint):
    j["state"] = obj.state
    j["time"] = obj.time
    if obj.value is not None:
        j["value"] = obj.value
    if obj.error is not None:
        j["error"] = obj.error
    j["histograms"] = []
    for item in obj.histograms:
        jj = {}
        Histogram_to_json(jj,item)
        j["histograms"].append(jj)


# Forward declaration
class Parameter: pass
class Parameter:

    
    def __init__ (
        self,
        value:float = nan,
        step:float = nan,
        min:float = nan,
        max:float = nan
    ):
        self.value : float = value
        self.step : float = step
        self.min : float = min
        self.max : float = max
        pass

    def __eq__ (self, other):
        if self.value != other.value: return False
        if self.step != other.step: return False
        if self.min != other.min: return False
        if self.max != other.max: return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return Parameter_to_json_string(self)
def Parameter_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Parameter()
    Parameter_from_json(j,obj)
    return obj

def Parameter_to_json_string (self:Parameter):
    j = {}
    Parameter_to_json(j,self)
    return json.dumps(j)
def Parameter_from_json (j:dict, obj:Parameter):
    assert isinstance(obj,Parameter)
    obj.value = j["value"]
    obj.step = j["step"]
    obj.min = j["min"]
    obj.max = j["max"]
def Parameter_to_json(j:dict, obj:Parameter):
    j["value"] = obj.value
    j["step"] = obj.step
    j["min"] = obj.min
    j["max"] = obj.max


# Forward declaration
class Model: pass
class Model:

    
    def __init__ (
        self,
        TimeStart:float = nan,
        TimeSteps:int = 0,
        NumPaths:int = 0,
        updaters:list[Updater] = [],
        evaluations:list[EvaluationPoint] = [],
        RandomSeed:int = -1,
        RunTimeoutSeconds:float = 1,
        MemoryLimitKB:int = 1
    ):
        self.TimeStart : float = TimeStart
        self.TimeSteps : int = TimeSteps
        self.NumPaths : int = NumPaths
        self.updaters : list[Updater] = deepcopy(updaters)
        self.evaluations : list[EvaluationPoint] = deepcopy(evaluations)
        self.RandomSeed : int = RandomSeed
        self.RunTimeoutSeconds : float = RunTimeoutSeconds
        self.MemoryLimitKB : int = MemoryLimitKB
        pass

    def GetNumberOfUpdaters (
        self,
    ):
        
        return len(self.updaters)
        
        pass

    def GetNumberOfStates (
        self,
    ):
        
        return len([u for u in self.updaters if u.HasState()])
        
        pass

    def Add (
        self,
        updater,
    ):
        
        self.updaters.append(updater)
        updater._equation = self.GetNumberOfUpdaters()-1
        updater._state = self.GetNumberOfStates()-1 if updater.HasState() else None
        return updater
        
        pass

    def __eq__ (self, other):
        if self.TimeStart != other.TimeStart: return False
        if self.TimeSteps != other.TimeSteps: return False
        if self.NumPaths != other.NumPaths: return False
        if self.updaters != other.updaters: return False
        if self.evaluations != other.evaluations: return False
        if self.RandomSeed != other.RandomSeed: return False
        if self.RunTimeoutSeconds != other.RunTimeoutSeconds: return False
        if self.MemoryLimitKB != other.MemoryLimitKB: return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return Model_to_json_string(self)
def Model_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Model()
    Model_from_json(j,obj)
    return obj

def Model_to_json_string (self:Model):
    j = {}
    Model_to_json(j,self)
    return json.dumps(j)
def Model_from_json (j:dict, obj:Model):
    assert isinstance(obj,Model)
    obj.TimeStart = j["TimeStart"]
    obj.TimeSteps = j["TimeSteps"]
    obj.NumPaths = j["NumPaths"]
    obj.updaters = []
    for item in j["updaters"]:
        v = Updater()
        Updater_from_json(item,v)
        obj.updaters.append(v)
    obj.evaluations = []
    for item in j["evaluations"]:
        v = EvaluationPoint()
        EvaluationPoint_from_json(item,v)
        obj.evaluations.append(v)
    obj.RandomSeed = j["RandomSeed"]
    obj.RunTimeoutSeconds = j["RunTimeoutSeconds"]
    obj.MemoryLimitKB = j["MemoryLimitKB"]
def Model_to_json(j:dict, obj:Model):
    j["TimeStart"] = obj.TimeStart
    j["TimeSteps"] = obj.TimeSteps
    j["NumPaths"] = obj.NumPaths
    j["updaters"] = []
    for item in obj.updaters:
        jj = {}
        Updater_to_json(jj,item)
        j["updaters"].append(jj)
    j["evaluations"] = []
    for item in obj.evaluations:
        jj = {}
        EvaluationPoint_to_json(jj,item)
        j["evaluations"].append(jj)
    j["RandomSeed"] = obj.RandomSeed
    j["RunTimeoutSeconds"] = obj.RunTimeoutSeconds
    j["MemoryLimitKB"] = obj.MemoryLimitKB


# Forward declaration
class Result: pass
class Result:

    
    def __init__ (
        self,
        n:int = 0,
        mean:float = nan,
        stddev:float = nan,
        skewness:float = nan
    ):
        self.n : int = n
        self.mean : float = mean
        self.stddev : float = stddev
        self.skewness : float = skewness
        pass

    def GetMean (
        self,
    ):
        
        return self.mean
        
        pass

    def GetMeanError (
        self,
    ):
        
        return nan if self.n<=0 else self.stddev/math.sqrt(self.n)
        
        pass

    def GetStdDev (
        self,
    ):
        
        return self.stddev
        
        pass

    def GetSkewness (
        self,
    ):
        
        return self.skewness
        
        pass

    def __eq__ (self, other):
        if self.n != other.n: return False
        if self.mean != other.mean: return False
        if self.stddev != other.stddev: return False
        if self.skewness != other.skewness: return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return Result_to_json_string(self)
def Result_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Result()
    Result_from_json(j,obj)
    return obj

def Result_to_json_string (self:Result):
    j = {}
    Result_to_json(j,self)
    return json.dumps(j)
def Result_from_json (j:dict, obj:Result):
    assert isinstance(obj,Result)
    obj.n = j["n"]
    obj.mean = j["mean"]
    obj.stddev = j["stddev"]
    obj.skewness = j["skewness"]
def Result_to_json(j:dict, obj:Result):
    j["n"] = obj.n
    j["mean"] = obj.mean
    j["stddev"] = obj.stddev
    j["skewness"] = obj.skewness


# Forward declaration
class EvaluationResults: pass
class EvaluationResults:

    
    def __init__ (
        self,
        names:list[str] = [],
        npaths:list[int] = [],
        mean:list[float] = [],
        stddev:list[float] = [],
        skewness:list[float] = [],
        time_points:list[float] = [],
        time_steps:list[int] = [],
        histograms:list[Histogram] = [],
        model:Model|None = None
    ):
        self.names : list[str] = names
        self.npaths : list[int] = npaths
        self.mean : list[float] = mean
        self.stddev : list[float] = stddev
        self.skewness : list[float] = skewness
        self.time_points : list[float] = time_points
        self.time_steps : list[int] = time_steps
        self.histograms : list[Histogram] = deepcopy(histograms)
        self.model : Model|None = deepcopy(model)
        pass

    def GetNumberOfStates (
        self,
    ):
        
        return len(self.names)
        
        pass

    def GetNumberOfEvaluations (
        self,
    ):
        
        return len(self.time_points)
        
        pass

    def Index (
        self,
        state,
        point,
    ):
        
        if not (state>=0 and state<self.GetNumberOfStates() and point>=0 and point<self.GetNumberOfEvaluations()):
            raise ValueError()
        return point*self.GetNumberOfStates() + state
        
        pass

    def GetStateEvaluationResult (
        self,
        state,
        point,
    ):
        
        n = self.Index(state,point)
        return Result(self.npaths[n],self.mean[n],self.stddev[n],self.skewness[n])
        
        pass

    def df (
        self,
    ):
        
        data = []
        for j in range(self.GetNumberOfEvaluations()):
            for i in range(self.GetNumberOfStates()):
                n = self.Index(i,j)
                item = {
                    'name': self.names[i],
                    'title': '',
                    'state': i,
                    'time': self.time_points[j],
                    'step': self.time_steps[j],
                    'npaths': self.npaths[n],
                    'mean':self.mean[n],
                    'mean_error': None if self.stddev[n] is None else self.stddev[n]/math.sqrt(self.npaths[n]),
                    'stddev': self.stddev[n],
                    'skewness': self.skewness[n]
                }
                # if self.model:
                #     item['title'] = self.model._titles.get(i,'')
                data.append(item)
        return pd.DataFrame(data)
        
        pass

    def __eq__ (self, other):
        if self.names != other.names: return False
        if self.npaths != other.npaths: return False
        if self.mean != other.mean: return False
        if self.stddev != other.stddev: return False
        if self.skewness != other.skewness: return False
        if self.time_points != other.time_points: return False
        if self.time_steps != other.time_steps: return False
        if self.histograms != other.histograms: return False
        if self.model != other.model: return False
        return True
    def __neq__ (self, other):
        return not self==other
    def json (self) -> str:
        return EvaluationResults_to_json_string(self)
def EvaluationResults_from_json_string (jstr):
    j = json.loads(jstr)
    obj = EvaluationResults()
    EvaluationResults_from_json(j,obj)
    return obj

def EvaluationResults_to_json_string (self:EvaluationResults):
    j = {}
    EvaluationResults_to_json(j,self)
    return json.dumps(j)
def EvaluationResults_from_json (j:dict, obj:EvaluationResults):
    assert isinstance(obj,EvaluationResults)
    obj.names = j["names"]
    obj.npaths = j["npaths"]
    obj.mean = j["mean"]
    obj.stddev = j["stddev"]
    obj.skewness = j["skewness"]
    obj.time_points = j["time_points"]
    obj.time_steps = j["time_steps"]
    obj.histograms = []
    for item in j["histograms"]:
        v = Histogram()
        Histogram_from_json(item,v)
        obj.histograms.append(v)
    if j.get("model",None) is not None:
        obj.model = Model()
        Model_from_json(j["model"],obj.model)
def EvaluationResults_to_json(j:dict, obj:EvaluationResults):
    j["names"] = obj.names
    j["npaths"] = obj.npaths
    j["mean"] = obj.mean
    j["stddev"] = obj.stddev
    j["skewness"] = obj.skewness
    j["time_points"] = obj.time_points
    j["time_steps"] = obj.time_steps
    j["histograms"] = []
    for item in obj.histograms:
        jj = {}
        Histogram_to_json(jj,item)
        j["histograms"].append(jj)
    if obj.model is not None:
        jj = {}
        Model_to_json(jj,obj.model)
        j["model"] = jj



def EvaluationResults_from_response(r,model=None):
    er = EvaluationResults_from_json_string(r.text)
    er.model = model
    return er

