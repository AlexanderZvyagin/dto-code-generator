
# This is an automatically generated file.
from copy import deepcopy
import math
from math import nan
import json
try:
    import pandas as pd
except:
    print('Warning: "pandas" package was not found.')


class UpdaterDoc:

    
    def __init__ (
        self,
        name_:str = "",
        title_:str = "",
        doc_md_:str = "",
        start_:str = "",
        nargs_min_:int = -88,
        nrefs_min_:int = -88
    ):
        self.name : str = name_
        self.title : str = title_
        self.doc_md : str = doc_md_
        self.start : str = start_
        self.nargs_min : int = nargs_min_
        self.nrefs_min : int = nrefs_min_
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


class UpdaterDto:

    
    def __init__ (
        self,
        name_:str = "",
        refs_:list[int]|None = None,
        args_:list[float]|None = None,
        start_:float|None = None
    ):
        self.name : str = name_
        self.refs : list[int]|None = refs_
        self.args : list[float]|None = args_
        self.start : float|None = start_
        pass

    def __eq__ (self, other):
        if self.name != other.name: return False
        if self.refs != other.refs: return False
        if self.args != other.args: return False
        if self.start != other.start: return False
        return True
    def __neq__ (self, other):
        return not self==other
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
    obj.refs = j.get("refs",None)
    obj.args = j.get("args",None)
    obj.start = j.get("start",None)
def UpdaterDto_to_json(j:dict, obj:UpdaterDto):
    j["name"] = obj.name
    if obj.refs is not None:
        j["refs"] = obj.refs
    if obj.args is not None:
        j["args"] = obj.args
    if obj.start is not None:
        j["start"] = obj.start


class Updater (UpdaterDto):

    
    def __init__ (
        self,
        name:str = "",
        refs:list[int] = [],
        args:list[float] = [],
        start:float|None = None
    ):
        super().__init__(
            name,
            refs,
            args,
            start,
        )
        self._equation : int = -88
        self._state : int = -88
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


class IndependentGaussian (Updater):

    
    def __init__ (
        self,
        refs_:list[int] = []
    ):
        super().__init__(
            "IndependentGaussian",
            refs_,
            [],
            -88,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
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


class CorrelatedGaussian (Updater):

    
    def __init__ (
        self,
        correlation:float = nan,
        state1:int = -88,
        state2:int = -88
    ):
        super().__init__(
            "CorrelatedGaussian",
            [state1,state2],
            [correlation],
            -88,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
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


class BrownianMotion (Updater):

    
    def __init__ (
        self,
        start_:float = nan,
        drift_:float = nan,
        diffusion_:float = nan
    ):
        super().__init__(
            "BrownianMotion",
            [],
            [drift_,diffusion_],
            start_,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
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


class BrownianMotionRef (Updater):

    
    def __init__ (
        self,
        start_:float = nan,
        drift_:int = -88,
        diffusion_:int = -88
    ):
        super().__init__(
            "BrownianMotion",
            [drift_,diffusion_],
            [],
            start_,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
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


class GeometricalBrownianMotion (Updater):

    
    def __init__ (
        self,
        start_:float = nan,
        drift_:float = nan,
        diffusion_:float = nan
    ):
        super().__init__(
            "GeometricalBrownianMotion",
            [],
            [drift_,diffusion_],
            start_,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
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


class GeometricalBrownianMotionRef (Updater):

    
    def __init__ (
        self,
        start_:float = nan,
        drift_:int = -88,
        diffusion_:int = -88
    ):
        super().__init__(
            "GeometricalBrownianMotion",
            [drift_,diffusion_],
            [],
            start_,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
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


class ZeroCouponBond (Updater):

    
    def __init__ (
        self,
        underlying_:int = -88,
        start_:float = nan
    ):
        super().__init__(
            "ZeroCouponBond",
            [underlying_],
            [],
            start_,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
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


class Option (Updater):

    
    def __init__ (
        self,
        underlying_:int = -88,
        strike_:float = nan,
        call_put_:int = -88
    ):
        super().__init__(
            "Option",
            [underlying_],
            [strike_,call_put_],
            None,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
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


class Barrier (Updater):

    
    def __init__ (
        self,
        underlying:int = -88,
        start:float = nan,
        level:float = nan,
        direction:int = -88,
        action:int = -88,
        value:float = nan
    ):
        super().__init__(
            "Barrier",
            [underlying],
            [level,value,direction,action],
            start,
        )
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        return True
    def __neq__ (self, other):
        return not self==other
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
    else:
        obj.y = None
def Histogram_to_json(j:dict, obj:Histogram):
    jj = {}
    HistogramAxis_to_json(jj,obj.x)
    j["x"] = jj
    if obj.y is not None:
        jj = {}
        HistogramAxis_to_json(jj,obj.y)
        j["y"] = jj


class EvaluationPoint:

    
    def __init__ (
        self,
        state_:int = -88,
        time_:float = nan,
        value_:float|None = None,
        error_:float|None = None,
        histograms_:list[Histogram] = []
    ):
        self.state : int = state_
        self.time : float = time_
        self.value : float|None = value_
        self.error : float|None = error_
        self.histograms : list[Histogram] = deepcopy(histograms_)
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
    obj.value = j.get("value",None)
    obj.error = j.get("error",None)
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


class Parameter:

    
    def __init__ (
        self,
        value_:float = nan,
        step_:float = nan,
        min_:float = nan,
        max_:float = nan
    ):
        self.value : float = value_
        self.step : float = step_
        self.min : float = min_
        self.max : float = max_
        pass

    def __eq__ (self, other):
        if self.value != other.value: return False
        if self.step != other.step: return False
        if self.min != other.min: return False
        if self.max != other.max: return False
        return True
    def __neq__ (self, other):
        return not self==other
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


class Model:

    
    def __init__ (
        self,
        TimeStart_:float = nan,
        TimeSteps_:int = 0,
        NumPaths_:int = 0,
        updaters_:list[Updater] = [],
        evaluations_:list[EvaluationPoint] = [],
        RunTimeoutSeconds_:float = 1,
        MemoryLimitKB_:int = 1
    ):
        self.TimeStart : float = TimeStart_
        self.TimeSteps : int = TimeSteps_
        self.NumPaths : int = NumPaths_
        self.updaters : list[Updater] = deepcopy(updaters_)
        self.evaluations : list[EvaluationPoint] = deepcopy(evaluations_)
        self.RunTimeoutSeconds : float = RunTimeoutSeconds_
        self.MemoryLimitKB : int = MemoryLimitKB_
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
        if self.RunTimeoutSeconds != other.RunTimeoutSeconds: return False
        if self.MemoryLimitKB != other.MemoryLimitKB: return False
        return True
    def __neq__ (self, other):
        return not self==other
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
    for item in j["updaters"]:
        v = Updater()
        Updater_from_json(item,v)
        obj.updaters.append(v)
    for item in j["evaluations"]:
        v = EvaluationPoint()
        EvaluationPoint_from_json(item,v)
        obj.evaluations.append(v)
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
    j["RunTimeoutSeconds"] = obj.RunTimeoutSeconds
    j["MemoryLimitKB"] = obj.MemoryLimitKB


class Result:

    
    def __init__ (
        self,
        n_:int = 0,
        mean_:float = nan,
        stddev_:float = nan,
        skewness_:float = nan
    ):
        self.n : int = n_
        self.mean : float = mean_
        self.stddev : float = stddev_
        self.skewness : float = skewness_
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


class EvaluationResults:

    
    def __init__ (
        self,
        names_:list[str] = [],
        npaths_:list[int] = [],
        mean_:list[float] = [],
        stddev_:list[float] = [],
        skewness_:list[float] = [],
        time_points_:list[float] = [],
        time_steps_:list[int] = [],
        histograms_:list[Histogram] = [],
        model_:Model|None = None
    ):
        self.names : list[str] = names_
        self.npaths : list[int] = npaths_
        self.mean : list[float] = mean_
        self.stddev : list[float] = stddev_
        self.skewness : list[float] = skewness_
        self.time_points : list[float] = time_points_
        self.time_steps : list[int] = time_steps_
        self.histograms : list[Histogram] = deepcopy(histograms_)
        self.model : Model|None = deepcopy(model_)
        pass

    def NumStates (
        self,
    ):
        
        return len(self.names)
        
        pass

    def NumEvaluations (
        self,
    ):
        
        return len(self.time_points)
        
        pass

    def Index (
        self,
        state,
        point,
    ):
        
        if not (state>=0 and state<self.NumStates() and point>=0 and point<self.NumEvaluations()):
            raise ValueError()
        return point*self.NumStates() + state
        
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
        for j in range(self.NumEvaluations()):
            for i in range(self.NumStates()):
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
                if self.model:
                    item['title'] = self.model._titles.get(i,'')
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
    for item in j["histograms"]:
        v = Histogram()
        Histogram_from_json(item,v)
        obj.histograms.append(v)
    if j.get("model",None) is not None:
        obj.model = Model()
        Model_from_json(j["model"],obj.model)
    else:
        obj.model = None
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


