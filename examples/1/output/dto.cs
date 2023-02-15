public class UpdaterDoc {

    public string name;
    public string title;
    public string doc_md;
    public string start;
    public int nargs_min;
    public int nrefs_min;

    // Function_csharp UpdaterDoc

};

public class UpdaterDto {

    public string name;
    public List<int> refs;
    public List<float> args;
    public float start;

    // Function_csharp UpdaterDto

};

public class Updater: UpdaterDto {

    public int _equation;
    public int _state;

    // Function_csharp Updater

    // Function_csharp GetStateNumber

};

public class IndependentGaussian: Updater {


    // Function_csharp IndependentGaussian

};

public class CorrelatedGaussian: Updater {


    // Function_csharp CorrelatedGaussian

};

public class Barrier: Updater {


    // Function_csharp Barrier

};

public class HistogramAxis {

    public int state;
    public int nbins;
    public float min;
    public float max;

    // Function_csharp HistogramAxis

};

public class Histogram {

    public HistogramAxis x;
    public HistogramAxis y;

    // Function_csharp Histogram

};

public class EvaluationPoint {

    public int state;
    public float time;
    public float value;
    public float error;

    // Function_csharp EvaluationPoint

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

    // Function_csharp EvaluationResults

};

public class Parameter {

    public float value;
    public float step;
    public float min;
    public float max;

    // Function_csharp Parameter

};

public class Model {

    public float TimeStart;
    public int TimeSteps;
    public int NumPaths;
    public List<Updater> updaters;
    public List<EvaluationPoint> evaluations;
    public float RunTimeoutSeconds;
    public int MemoryLimitKB;

    // Function_csharp Model

};

