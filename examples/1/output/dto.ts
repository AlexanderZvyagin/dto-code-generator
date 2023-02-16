// This is an automatically generated file.

class UpdaterDoc {

    name : string;
    title : string;
    doc_md : string;
    start : string;
    nargs_min : number;
    nrefs_min : number;

    constructor(
        name_ : string  = "",
        title_ : string  = "",
        doc_md_ : string  = "",
        start_ : string  = "",
        nargs_min_ : number  = -88,
        nrefs_min_ : number  = -88,
    ){
        this.name = name_;
        this.title = title_;
        this.doc_md = doc_md_;
        this.start = start_;
        this.nargs_min = nargs_min_;
        this.nrefs_min = nrefs_min_;
    
    }

}

class UpdaterDto {

    name : string;
    refs : number[]|undefined;
    args : number[]|undefined;
    start : number|undefined;

    constructor(
        name_ : string  = "",
        refs_ : number[]|undefined ,
        args_ : number[]|undefined ,
        start_ : number|undefined ,
    ){
        this.name = name_;
        this.refs = refs_;
        this.args = args_;
        this.start = start_;
    
    }

}

class Updater extends UpdaterDto {

    _equation : number;
    _state : number;

    constructor(
        name : string  = "",
        refs : number[]  = [],
        args : number[]  = [],
        start : number  = Number.NaN,
    ){
        super(
            name,
            refs,
            args,
            start,
        );
        this._equation = -88;
        this._state = -88;
    
    }

    GetStateNumber (
    ) : number  {
        
        if(this._state<0)
            throw new Error(`Updater ${this.name} has no state.`);
        return this._state;
        
    }

}

class IndependentGaussian extends Updater {


    constructor(
        refs_ : number[]  = [],
    ){
        super(
            "IndependentGaussian",
            refs_,
            [],
            -88,
        );
    
    }

}

class CorrelatedGaussian extends Updater {


    constructor(
        correlation : number  = Number.NaN,
        state1 : number  = -88,
        state2 : number  = -88,
    ){
        super(
            "CorrelatedGaussian",
            [state1,state2],
            [correlation],
            -88,
        );
    
    }

}

class Barrier extends Updater {


    constructor(
        underlying : number  = -88,
        start : number  = Number.NaN,
        level : number  = Number.NaN,
        direction : number  = -88,
        action : number  = -88,
        value : number  = Number.NaN,
    ){
        super(
            "Barrier",
            [underlying],
            [level,value,direction,action],
            start,
        );
    
    }

}

class HistogramAxis {

    state : number;
    nbins : number;
    min : number;
    max : number;

    constructor(
        _state : number  = -88,
        _nbins : number  = -88,
        _min : number  = -88,
        _max : number  = -88,
    ){
        this.state = _state;
        this.nbins = _nbins;
        this.min = _min;
        this.max = _max;
    
    }

}

class Histogram {

    x : HistogramAxis;
    y : HistogramAxis;

    constructor(
        x : HistogramAxis  = new HistogramAxis(),
        y : HistogramAxis  = new HistogramAxis(),
    ){
        this.x = x;
        this.y = y;
    
    }

}

class EvaluationPoint {

    state : number;
    time : number;
    value : number;
    error : number;

    constructor(
        state_ : number  = -88,
        time_ : number  = Number.NaN,
        value_ : number  = Number.NaN,
        error_ : number  = Number.NaN,
    ){
        this.state = state_;
        this.time = time_;
        this.value = value_;
        this.error = error_;
    
    }

}

class EvaluationResults {

    names : string[];
    npaths : number[];
    mean : number[];
    stddev : number[];
    skewness : number[];
    time_points : number[];
    time_steps : number[];
    histograms : Histogram[];

    constructor(
        names_ : string[]  = [],
        npaths_ : number[]  = [],
        mean_ : number[]  = [],
        stddev_ : number[]  = [],
        skewness_ : number[]  = [],
        time_points_ : number[]  = [],
        time_steps_ : number[]  = [],
        histograms_ : Histogram[]  = [],
    ){
        this.names = names_;
        this.npaths = npaths_;
        this.mean = mean_;
        this.stddev = stddev_;
        this.skewness = skewness_;
        this.time_points = time_points_;
        this.time_steps = time_steps_;
        this.histograms = histograms_;
    
    }

}

class Parameter {

    value : number;
    step : number;
    min : number;
    max : number;

    constructor(
        value_ : number  = Number.NaN,
        step_ : number  = Number.NaN,
        min_ : number  = Number.NaN,
        max_ : number  = Number.NaN,
    ){
        this.value = value_;
        this.step = step_;
        this.min = min_;
        this.max = max_;
    
    }

}

class Model {

    TimeStart : number;
    TimeSteps : number;
    NumPaths : number;
    updaters : Updater[];
    evaluations : EvaluationPoint[];
    RunTimeoutSeconds : number;
    MemoryLimitKB : number;

    constructor(
        TimeStart_ : number  = Number.NaN,
        TimeSteps_ : number  = 0,
        NumPaths_ : number  = 0,
        updaters_ : Updater[]  = [],
        evaluations_ : EvaluationPoint[]  = [],
        RunTimeoutSeconds_ : number  = 1,
        MemoryLimitKB_ : number  = 1,
    ){
        this.TimeStart = TimeStart_;
        this.TimeSteps = TimeSteps_;
        this.NumPaths = NumPaths_;
        this.updaters = updaters_;
        this.evaluations = evaluations_;
        this.RunTimeoutSeconds = RunTimeoutSeconds_;
        this.MemoryLimitKB = MemoryLimitKB_;
    
    }

}

export {
    UpdaterDoc,
    UpdaterDto,
    Updater,
    IndependentGaussian,
    CorrelatedGaussian,
    Barrier,
    HistogramAxis,
    Histogram,
    EvaluationPoint,
    EvaluationResults,
    Parameter,
    Model,
}
