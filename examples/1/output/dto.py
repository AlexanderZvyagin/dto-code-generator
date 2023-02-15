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
        self.name = name_
        self.title = title_
        self.doc_md = doc_md_
        self.start = start_
        self.nargs_min = nargs_min_
        self.nrefs_min = nrefs_min_
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
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
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
        refs_ = [],
        args_ = [],
        start_ = nan
    ):
        self.name = name_
        self.refs = refs_
        self.args = args_
        self.start = start_
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
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
def UpdaterDto_from_json (j, obj):
    obj.name = j["name"]
    obj.refs = j["refs"]
    obj.args = j["args"]
    obj.start = j["start"]
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
        self._equation = -88
        self._state = -88
        pass

    def GetStateNumber (
        self,
    ):
        
        if self._state<0:
            raise Exception(f'Updater {self.name} has no state.')
        return self._state
        
        pass

    def __eq__ (self, other):
        if not super().__eq__(other): return False
        if self._equation != other._equation: return False
        if self._state != other._state: return False
        return True
    def __neq__ (self, other):
        return not (self==other)
def Updater_to_json_string (self):
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
def Updater_from_json (j, obj):
    UpdaterDto_from_json(j,obj)
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
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
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
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
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
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
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
        self.state = _state
        self.nbins = _nbins
        self.min = _min
        self.max = _max
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
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
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
        self.x = x
        self.y = y
        pass

    def __eq__ (self, other):
        if self.x != other.x: return False
        if self.y != other.y: return False
        return True
    def __neq__ (self, other):
        return not (self==other)
def Histogram_to_json_string (self):
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
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
        self.state = state_
        self.time = time_
        self.value = value_
        self.error = error_
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
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
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
        self.names = names_
        self.npaths = npaths_
        self.mean = mean_
        self.stddev = stddev_
        self.skewness = skewness_
        self.time_points = time_points_
        self.time_steps = time_steps_
        self.histograms = histograms_
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
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
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
        self.value = value_
        self.step = step_
        self.min = min_
        self.max = max_
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
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
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
        self.TimeStart = TimeStart_
        self.TimeSteps = TimeSteps_
        self.NumPaths = NumPaths_
        self.updaters = updaters_
        self.evaluations = evaluations_
        self.RunTimeoutSeconds = RunTimeoutSeconds_
        self.MemoryLimitKB = MemoryLimitKB_
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
    print(type(self))
    for k,v in self.__dict__.items():
        print(k,v)
    return json.dumps(self,default=lambda x: x.__dict__)
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


