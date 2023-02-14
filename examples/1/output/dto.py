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

def UpdaterDoc_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

class UpdaterDto:

    
    def __init__ (
        self,
        name_ = "",
        refs_ = {},
        args_ = {},
        start_ = nan
    ):
        self.name = name_
        self.refs = refs_
        self.args = args_
        self.start = start_
        pass

def UpdaterDto_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

class Updater (UpdaterDto):

    
    def __init__ (
        self,
        name = "",
        refs = {},
        args = {},
        start = nan
    ):
        super.__init__(
            name,
            refs,
            args,
            start,
        )
        pass

    def GetStateNumber (
        self,
    ):
        
        if self._state<0:
            raise Exception(f'Updater {self.name} has no state.')
        return self._state
        
        pass

def Updater_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

class IndependentGaussian (Updater):

    
    def __init__ (
        self,
        refs_ = {}
    ):
        super.__init__(
            "IndependentGaussian",
            refs_,
            {},
            -88,
        )
        pass

def IndependentGaussian_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

class CorrelatedGaussian (Updater):

    
    def __init__ (
        self,
        correlation = nan,
        state1 = -88,
        state2 = -88
    ):
        super.__init__(
            "CorrelatedGaussian",
            {state1,state2},
            {correlation},
            -88,
        )
        pass

def CorrelatedGaussian_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

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
        super.__init__(
            "Barrier",
            {underlying},
            {level,value,direction,action},
            start,
        )
        pass

def Barrier_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

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

def HistogramAxis_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

class Histogram:

    
    def __init__ (
        self,
    ):
        pass

def Histogram_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

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

def EvaluationPoint_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

class EvaluationResults:

    
    def __init__ (
        self,
        names_ = {},
        npaths_ = {},
        mean_ = {},
        stddev_ = {},
        skewness_ = {},
        time_points_ = {},
        time_steps_ = {},
        histograms_ = {}
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

def EvaluationResults_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

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

def Parameter_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

class Model:

    
    def __init__ (
        self,
        TimeStart_ = nan,
        TimeSteps_ = 0,
        NumPaths_ = 0,
        updaters_ = {},
        evaluations_ = {},
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

def Model_to_JSON (self):
    return json.dumps(self,default=lambda o: {k:v for k,v in o.__dict__.items() if k[0]!='_'})

