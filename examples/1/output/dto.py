# This is an automatically generated file.
from math import nan
import json
# 1

class UpdaterDoc:

    
    def __init__ (
        self,
        name_ = "",
        title_ = "",
        doc_md_ = "",
        start_ = "",
        nargs_min_ = -88,
        nrefs_min_ = -88
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
        return not (self==other)
def UpdaterDoc_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def UpdaterDoc_from_json (j, obj):
    obj.name = j["name"]
    obj.title = j["title"]
    obj.doc_md = j["doc_md"]
    obj.start = j["start"]
    obj.nargs_min = j["nargs_min"]
    obj.nrefs_min = j["nrefs_min"]
def UpdaterDoc_from_json_string (jstr):
    j = json.loads(jstr)
    obj = UpdaterDoc()
    UpdaterDoc_from_json(j,obj)
    return obj


class UpdaterDto:

    
    def __init__ (
        self,
        name_ = "",
        refs_ = None,
        args_ = None,
        start_ = None
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
        return not (self==other)
def UpdaterDto_to_json_string (self):
    def is_serialisable(k,v):
        if k in ['refs', 'args', 'start'] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def UpdaterDto_from_json (j, obj):
    obj.name = j["name"]
    obj.refs = j.get("refs",None)
    obj.args = j.get("args",None)
    obj.start = j.get("start",None)
def UpdaterDto_from_json_string (jstr):
    j = json.loads(jstr)
    obj = UpdaterDto()
    UpdaterDto_from_json(j,obj)
    return obj


class Updater (UpdaterDto):

    
    def __init__ (
        self,
        name = "",
        refs = [],
        args = [],
        start = nan
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

    def HasState (
        self,
    ):
        
        return self._state>=0
        
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        if self._equation != other._equation: return False
        if self._state != other._state: return False
        return True
    def __neq__ (self, other):
        return not (self==other)
def Updater_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def Updater_from_json (j, obj):
    UpdaterDto_from_json(j,obj)
    obj._equation = j["_equation"]
    obj._state = j["_state"]
def Updater_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Updater()
    Updater_from_json(j,obj)
    return obj


class IndependentGaussian (Updater):

    
    def __init__ (
        self,
        refs_ = []
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
        return not (self==other)
def IndependentGaussian_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def IndependentGaussian_from_json (j, obj):
    Updater_from_json(j,obj)
def IndependentGaussian_from_json_string (jstr):
    j = json.loads(jstr)
    obj = IndependentGaussian()
    IndependentGaussian_from_json(j,obj)
    return obj


class CorrelatedGaussian (Updater):

    
    def __init__ (
        self,
        correlation = nan,
        state1 = -88,
        state2 = -88
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
        return not (self==other)
def CorrelatedGaussian_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def CorrelatedGaussian_from_json (j, obj):
    Updater_from_json(j,obj)
def CorrelatedGaussian_from_json_string (jstr):
    j = json.loads(jstr)
    obj = CorrelatedGaussian()
    CorrelatedGaussian_from_json(j,obj)
    return obj


class Barrier (Updater):

    
    def __init__ (
        self,
        underlying = -88,
        start = nan,
        level = nan,
        direction = -88,
        action = -88,
        value = nan
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
        return not (self==other)
def Barrier_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def Barrier_from_json (j, obj):
    Updater_from_json(j,obj)
def Barrier_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Barrier()
    Barrier_from_json(j,obj)
    return obj


class HistogramAxis:

    
    def __init__ (
        self,
        _state = -88,
        _nbins = -88,
        _min = -88,
        _max = -88
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
        return not (self==other)
def HistogramAxis_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def HistogramAxis_from_json (j, obj):
    obj.state = j["state"]
    obj.nbins = j["nbins"]
    obj.min = j["min"]
    obj.max = j["max"]
def HistogramAxis_from_json_string (jstr):
    j = json.loads(jstr)
    obj = HistogramAxis()
    HistogramAxis_from_json(j,obj)
    return obj


class Histogram:

    
    def __init__ (
        self,
        x = HistogramAxis(),
        y = HistogramAxis()
    ):
        self.x : HistogramAxis = x
        self.y : HistogramAxis = y
        pass

    def __eq__ (self, other):
        if self.x != other.x: return False
        if self.y != other.y: return False
        return True
    def __neq__ (self, other):
        return not (self==other)
def Histogram_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def Histogram_from_json (j, obj):
    obj.x = j["x"]
    obj.y = j["y"]
def Histogram_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Histogram()
    Histogram_from_json(j,obj)
    return obj


class EvaluationPoint:

    
    def __init__ (
        self,
        state_ = -88,
        time_ = nan,
        value_ = nan,
        error_ = nan
    ):
        self.state : int = state_
        self.time : float = time_
        self.value : float = value_
        self.error : float = error_
        pass

    def __eq__ (self, other):
        if self.state != other.state: return False
        if self.time != other.time: return False
        if self.value != other.value: return False
        if self.error != other.error: return False
        return True
    def __neq__ (self, other):
        return not (self==other)
def EvaluationPoint_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def EvaluationPoint_from_json (j, obj):
    obj.state = j["state"]
    obj.time = j["time"]
    obj.value = j["value"]
    obj.error = j["error"]
def EvaluationPoint_from_json_string (jstr):
    j = json.loads(jstr)
    obj = EvaluationPoint()
    EvaluationPoint_from_json(j,obj)
    return obj


class EvaluationResults:

    
    def __init__ (
        self,
        names_ = [],
        npaths_ = [],
        mean_ = [],
        stddev_ = [],
        skewness_ = [],
        time_points_ = [],
        time_steps_ = [],
        histograms_ = []
    ):
        self.names : list[str] = names_
        self.npaths : list[int] = npaths_
        self.mean : list[float] = mean_
        self.stddev : list[float] = stddev_
        self.skewness : list[float] = skewness_
        self.time_points : list[float] = time_points_
        self.time_steps : list[int] = time_steps_
        self.histograms : list[Histogram] = histograms_
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
        return True
    def __neq__ (self, other):
        return not (self==other)
def EvaluationResults_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def EvaluationResults_from_json (j, obj):
    obj.names = j["names"]
    obj.npaths = j["npaths"]
    obj.mean = j["mean"]
    obj.stddev = j["stddev"]
    obj.skewness = j["skewness"]
    obj.time_points = j["time_points"]
    obj.time_steps = j["time_steps"]
    obj.histograms = j["histograms"]
def EvaluationResults_from_json_string (jstr):
    j = json.loads(jstr)
    obj = EvaluationResults()
    EvaluationResults_from_json(j,obj)
    return obj


class Parameter:

    
    def __init__ (
        self,
        value_ = nan,
        step_ = nan,
        min_ = nan,
        max_ = nan
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
        return not (self==other)
def Parameter_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def Parameter_from_json (j, obj):
    obj.value = j["value"]
    obj.step = j["step"]
    obj.min = j["min"]
    obj.max = j["max"]
def Parameter_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Parameter()
    Parameter_from_json(j,obj)
    return obj


class Model:

    
    def __init__ (
        self,
        TimeStart_ = nan,
        TimeSteps_ = 0,
        NumPaths_ = 0,
        updaters_ = [],
        evaluations_ = [],
        RunTimeoutSeconds_ = 1,
        MemoryLimitKB_ = 1
    ):
        self.TimeStart : float = TimeStart_
        self.TimeSteps : int = TimeSteps_
        self.NumPaths : int = NumPaths_
        self.updaters : list[Updater] = updaters_
        self.evaluations : list[EvaluationPoint] = evaluations_
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
        updater
    ):
        
        self.updaters.append(updater)
        # title = getattr(updater,'_title',None)
        # updater._equation = len(self.updaters)-1
        # updater._state = self.NumStatefulProcesses()-1 if updater.HasState() else None
        # self._titles[updater._state] = title
        # return updater
        
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
        return not (self==other)
def Model_to_json_string (self):
    def is_serialisable(k,v):
        if k in [] and v is None: return False
        if k in []: return False
        return True
    return json.dumps(self,default=lambda x: {k:v for k,v in x.__dict__.items() if is_serialisable(k,v) })
def Model_from_json (j, obj):
    obj.TimeStart = j["TimeStart"]
    obj.TimeSteps = j["TimeSteps"]
    obj.NumPaths = j["NumPaths"]
    obj.updaters = j["updaters"]
    obj.evaluations = j["evaluations"]
    obj.RunTimeoutSeconds = j["RunTimeoutSeconds"]
    obj.MemoryLimitKB = j["MemoryLimitKB"]
def Model_from_json_string (jstr):
    j = json.loads(jstr)
    obj = Model()
    Model_from_json(j,obj)
    return obj


