public class UpdaterDoc {

    public string name;
    public string title;
    public string doc_md;
    public string start;
    public int nargs_min;
    public int nrefs_min;

    
    UpdaterDoc (
        string name_ = Variable(name='name_', type='string', defval='', list=False, optional=False),
        string title_ = Variable(name='title_', type='string', defval='', list=False, optional=False),
        string doc_md_ = Variable(name='doc_md_', type='string', defval='', list=False, optional=False),
        string start_ = Variable(name='start_', type='string', defval='', list=False, optional=False),
        int nargs_min_ = Variable(name='nargs_min_', type='int', defval=-88, list=False, optional=False),
        int nrefs_min_ = Variable(name='nrefs_min_', type='int', defval=-88, list=False, optional=False)
    ){
    }

};

public class UpdaterDto {

    public string name;
    public List<int>? refs;
    public List<float>? args;
    public float? start;

    
    UpdaterDto (
        string name_ = Variable(name='name_', type='string', defval='', list=False, optional=False),
        List<int>? refs_ = {},
        List<float>? args_ = {},
        float? start_ = {}
    ){
    }

};

public class Updater: UpdaterDto {

    public int _equation;
    public int _state;

    
    Updater (
        string name = Variable(name='name', type='string', defval='', list=False, optional=False),
        List<int> refs = Variable(name='refs', type='int', defval=[], list=True, optional=False),
        List<float> args = Variable(name='args', type='float', defval=[], list=True, optional=False),
        float start = Variable(name='start', type='float', defval=nan, list=False, optional=False)
    ){
    }

    int GetStateNumber (
    ){
    }

};

public class IndependentGaussian: Updater {


    
    IndependentGaussian (
        List<int> refs_ = Variable(name='refs_', type='int', defval=[], list=True, optional=False)
    ){
    }

};

public class CorrelatedGaussian: Updater {


    
    CorrelatedGaussian (
        float correlation = Variable(name='correlation', type='float', defval=nan, list=False, optional=False),
        int state1 = Variable(name='state1', type='int', defval=-88, list=False, optional=False),
        int state2 = Variable(name='state2', type='int', defval=-88, list=False, optional=False)
    ){
    }

};

public class Barrier: Updater {


    
    Barrier (
        int underlying = Variable(name='underlying', type='int', defval=-88, list=False, optional=False),
        float start = Variable(name='start', type='float', defval=nan, list=False, optional=False),
        float level = Variable(name='level', type='float', defval=nan, list=False, optional=False),
        int direction = Variable(name='direction', type='int', defval=-88, list=False, optional=False),
        int action = Variable(name='action', type='int', defval=-88, list=False, optional=False),
        float value = Variable(name='value', type='float', defval=nan, list=False, optional=False)
    ){
    }

};

public class HistogramAxis {

    public int state;
    public int nbins;
    public float min;
    public float max;

    
    HistogramAxis (
        int _state = Variable(name='_state', type='int', defval=-88, list=False, optional=False),
        int _nbins = Variable(name='_nbins', type='int', defval=-88, list=False, optional=False),
        float _min = Variable(name='_min', type='float', defval=-88, list=False, optional=False),
        float _max = Variable(name='_max', type='float', defval=-88, list=False, optional=False)
    ){
    }

};

public class Histogram {

    public HistogramAxis x;
    public HistogramAxis y;

    
    Histogram (
        HistogramAxis x = Variable(name='x', type='HistogramAxis', defval=Variable(name='HistogramAxis()', type='type', defval=None, list=False, optional=False), list=False, optional=False),
        HistogramAxis y = Variable(name='y', type='HistogramAxis', defval=Variable(name='HistogramAxis()', type='type', defval=None, list=False, optional=False), list=False, optional=False)
    ){
    }

};

public class EvaluationPoint {

    public int state;
    public float time;
    public float value;
    public float error;

    
    EvaluationPoint (
        int state_ = Variable(name='state_', type='int', defval=-88, list=False, optional=False),
        float time_ = Variable(name='time_', type='float', defval=nan, list=False, optional=False),
        float value_ = Variable(name='value_', type='float', defval=nan, list=False, optional=False),
        float error_ = Variable(name='error_', type='float', defval=nan, list=False, optional=False)
    ){
    }

};

public class EvaluationResults {

    public List<string> names;
    public List<int> npaths;
    public List<float> mean;
    public List<float> stddev;
    public List<float> skewness;
    public List<float> time_points;
    public List<int> time_steps;
    public List<Histogram> histograms;

    
    EvaluationResults (
        List<string> names_ = Variable(name='names_', type='string', defval=[], list=True, optional=False),
        List<int> npaths_ = Variable(name='npaths_', type='int', defval=[], list=True, optional=False),
        List<float> mean_ = Variable(name='mean_', type='float', defval=[], list=True, optional=False),
        List<float> stddev_ = Variable(name='stddev_', type='float', defval=[], list=True, optional=False),
        List<float> skewness_ = Variable(name='skewness_', type='float', defval=[], list=True, optional=False),
        List<float> time_points_ = Variable(name='time_points_', type='float', defval=[], list=True, optional=False),
        List<int> time_steps_ = Variable(name='time_steps_', type='int', defval=[], list=True, optional=False),
        List<Histogram> histograms_ = Variable(name='histograms_', type='Histogram', defval=[], list=True, optional=False)
    ){
    }

};

public class Parameter {

    public float value;
    public float step;
    public float min;
    public float max;

    
    Parameter (
        float value_ = Variable(name='value_', type='float', defval=nan, list=False, optional=False),
        float step_ = Variable(name='step_', type='float', defval=nan, list=False, optional=False),
        float min_ = Variable(name='min_', type='float', defval=nan, list=False, optional=False),
        float max_ = Variable(name='max_', type='float', defval=nan, list=False, optional=False)
    ){
    }

};

public class Model {

    public float TimeStart;
    public int TimeSteps;
    public int NumPaths;
    public List<Updater> updaters;
    public List<EvaluationPoint> evaluations;
    public float RunTimeoutSeconds;
    public int MemoryLimitKB;

    
    Model (
        float TimeStart_ = Variable(name='TimeStart_', type='float', defval=nan, list=False, optional=False),
        int TimeSteps_ = Variable(name='TimeSteps_', type='int', defval=0, list=False, optional=False),
        int NumPaths_ = Variable(name='NumPaths_', type='int', defval=0, list=False, optional=False),
        List<Updater> updaters_ = Variable(name='updaters_', type='Updater', defval=[], list=True, optional=False),
        List<EvaluationPoint> evaluations_ = Variable(name='evaluations_', type='EvaluationPoint', defval=[], list=True, optional=False),
        float RunTimeoutSeconds_ = Variable(name='RunTimeoutSeconds_', type='float', defval=1, list=False, optional=False),
        int MemoryLimitKB_ = Variable(name='MemoryLimitKB_', type='int', defval=1, list=False, optional=False)
    ){
    }

    int GetNumberOfUpdaters (
    ){
        
        return updaters.Count();
        
    }

    void Add (
        Updater updater
    ){
    }

};

