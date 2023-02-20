#!/usr/bin/env python3

from cg import *
from math import nan

def create_dto(fname, languages):

    objs = [] # objects in the file

    obj = Struct('UpdaterDoc')
    obj.attributes.append(Variable('name','string'))
    obj.attributes.append(Variable('title','string'))
    obj.attributes.append(Variable('doc_md','string'))
    obj.attributes.append(Variable('start','string'))
    obj.attributes.append(Variable('nargs_min','int'))
    obj.attributes.append(Variable('nrefs_min','int'))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name_','string',''),
            Variable('title_','string',''),
            Variable('doc_md_','string',''),
            Variable('start_','string',''),
            Variable('nargs_min_','int',-88),
            Variable('nrefs_min_','int',-88)
        ],
        mapping = [
            ('name',[Variable('name_')]),
            ('title',[Variable('title_')]),
            ('doc_md',[Variable('doc_md_')]),
            ('start',[Variable('start_')]),
            ('nargs_min',[Variable('nargs_min_')]),
            ('nrefs_min',[Variable('nrefs_min_')]),
        ]
    ))
    objs.append(obj)

    obj = Struct('UpdaterDto')
    obj.attributes.append(Variable('name','string'))
    obj.attributes.append(Variable('refs','int', list=True, optional=True))
    obj.attributes.append(Variable('args','float', list=True, optional=True))
    obj.attributes.append(Variable('start','float',optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name_', 'string', ''),
            Variable(name='refs_', type='int', defval=None, list=True, optional=True),
            Variable('args_', 'float', defval=None, list=True, optional=True),
            Variable('start_', 'float', defval=None, optional=True)
        ],
        mapping = [
            ('name',[Variable('name_')]),
            ('refs',[Variable('refs_')]),
            ('args',[Variable('args_')]),
            ('start',[Variable('start_')]),
        ]
    ))
    objs.append(obj)
    UpdaterDto = obj

    obj = Struct('Updater',UpdaterDto)
    obj.attributes.append(Variable('_equation','int',skip_dto=True))
    obj.attributes.append(Variable('_state','int',skip_dto=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name','string',''),
            Variable('refs','int',[],list=True),
            Variable('args','float',[],list=True),
            Variable('start','float',None,optional=True),
        ],
        mapping = [
            (obj.base.name,[
                Variable('name'),
                Variable('refs'),
                Variable('args'),
                Variable('start'),
            ]),
            ('_equation',[-88]),
            ('_state',[-88]),
        ]
    ))
    obj.methods.append(Function (
        'GetStateNumber',
        'int',
        code = {
            'typescript':
'''
if(this._state<0)
    throw new Error(`Updater ${this.name} has no state.`);
return this._state;
''',
            'cpp':
'''
if(_state<0)
    throw std::runtime_error("An updater has no state.");
return _state;
''',
            'python':
'''
if self._state<0:
    raise Exception(f'Updater {self.name} has no state.')
return self._state
'''
        }
    ))

    obj.methods.append(Function (
        'GetEquationNumber',
        'int',
        code = {
            'typescript':
'''
if(this._equation<0)
    throw new Error(`Updater ${this.name} has no _equation.`);
return this._equation;
''',
            'cpp':
'''
if(_equation<0)
    throw std::runtime_error("An updater has no _equation.");
return _equation;
''',
            'python':
'''
if self._equation<0:
    raise Exception(f'Updater {self.name} has no _equation.')
return self._equation
'''
        }
    ))

    obj.methods.append(Function (
        'HasState',
        'boolean',
        const = True,
        code = {
            'python':
'''
return self.start is not None
''',
            'cpp':
'''
return start.has_value();
''',
            'typescript':
'''
return this.start !== undefined;
'''
        }
    ))

    obj.methods.append(Function (
        'GetStart',
        'float',
        const = True,
        code = {
            'python':
'''
if self.start is None:
    raise ValueError()
return self.start
''',
            'cpp':
'''
if( not start.has_value() )
    throw std::invalid_argument("start");
return start.value();
''',
            'typescript':
'''
if( this.start === undefined )
    throw new Error("start");
return this.start;
'''
        }
    ))

    objs.append(obj)
    Updater = obj

    objs.append(CodeBlock(code={
        'cpp': {'''
void from_json(const json &j, std::vector<Updater> &u) {
    for(auto v: j)
        u.push_back(v);
}
'''
        }
    }))

    obj = Struct('IndependentGaussian',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('refs_','int'  ,defval=[], list=True),
        ],
        mapping = [(obj.base.name,[
            'IndependentGaussian',
            Variable('refs_'),
            [],
            -88 # FIXME: cannot use math.nan for the moment
        ])]
    ))
    objs.append(obj)
    
    obj = Struct('CorrelatedGaussian',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('correlation','float'  ,nan),
            Variable('state1','int'  ,-88),
            Variable('state2','int'  ,-88),
        ],
        mapping = [(obj.base.name,[
            'CorrelatedGaussian',
            [Variable('state1'),Variable('state2')],
            [Variable('correlation')],
            -88 # FIXME: cannot use math.nan for the moment
        ])]
    ))
    objs.append(obj)

    # TODO: add Linear1DInterpolation

    obj = Struct('BrownianMotion',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start_'     ,'float', nan),
            Variable('drift_'     ,'float', nan),
            Variable('diffusion_' ,'float', nan),
        ],
        mapping = [(obj.base.name,[
            'BrownianMotion',
            [], # refs
            [Variable('drift_'),Variable('diffusion_')], # args
            Variable('start_')
        ])]
    ))
    objs.append(obj)

    obj = Struct('BrownianMotionRef',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start_'     ,'float', nan),
            Variable('drift_'     ,'int'  , -88),
            Variable('diffusion_' ,'int'  , -88),
        ],
        mapping = [(obj.base.name,[
            'BrownianMotion',
            [Variable('drift_'),Variable('diffusion_')], # refs
            [], # args
            Variable('start_')
        ])]
    ))
    objs.append(obj)

    obj = Struct('GeometricalBrownianMotion',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start_'     ,'float', nan),
            Variable('drift_'     ,'float', nan),
            Variable('diffusion_' ,'float', nan),
        ],
        mapping = [(obj.base.name,[
            'GeometricalBrownianMotion',
            [], # refs
            [Variable('drift_'),Variable('diffusion_')], # args
            Variable('start_')
        ])]
    ))
    objs.append(obj)

    obj = Struct('GeometricalBrownianMotionRef',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start_'     ,'float', nan),
            Variable('drift_'     ,'int'  , -88),
            Variable('diffusion_' ,'int'  , -88),
        ],
        mapping = [(obj.base.name,[
            'GeometricalBrownianMotion',
            [Variable('drift_'),Variable('diffusion_')], # refs
            [], # args
            Variable('start_')
        ])]
    ))
    objs.append(obj)

    obj = Struct('ZeroCouponBond',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('underlying_','int'  , -88),
            Variable('start_'     ,'float', nan),
        ],
        mapping = [(obj.base.name,[
            'ZeroCouponBond',
            [Variable('underlying_')], # refs
            [], # args
            Variable('start_')
        ])]
    ))
    objs.append(obj)

    obj = Struct('Option',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('underlying_','int'  , -88),
            Variable('strike_'    ,'float', nan),
            Variable('call_put_'  ,'int',   -88),
        ],
        mapping = [(obj.base.name,[
            'Option',
            [Variable('underlying_')], # refs
            [Variable('strike_'),Variable('call_put_')], # args
            None # start
        ])]
    ))
    objs.append(obj)

    obj = Struct('Barrier',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('underlying','int'  ,-88),
            Variable('start'     ,'float',nan),
            Variable('level'     ,'float',nan),
            Variable('direction' ,'int'  ,-88),
            Variable('action'    ,'int'  ,-88),
            Variable('value'     ,'float',nan),
        ],
        mapping = [(obj.base.name,[
            'Barrier',
            [
                Variable('underlying')
            ],
            [
                Variable('level'),
                Variable('value'),
                Variable('direction'),
                Variable('action')
            ],
            Variable('start')
        ])]
    ))
    
    objs.append(obj)

    obj = Struct('HistogramAxis')
    HistogramAxis = obj
    obj.attributes.append(Variable('state','int'))
    obj.attributes.append(Variable('nbins','int'))
    obj.attributes.append(Variable('min','float'))
    obj.attributes.append(Variable('max','float'))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('_state','int',-88),
            Variable('_nbins','int',-88),
            Variable('_min'  ,'float',-88), # FIXME: cannot use math.nan for the moment
            Variable('_max'  ,'float',-88), # FIXME: cannot use math.nan for the moment
        ],
        mapping = [
            ('state',[Variable('_state')]),
            ('nbins',[Variable('_nbins')]),
            ('min',[Variable('_min')]),
            ('max',[Variable('_max')]),
        ]
    ))
    objs.append(obj)

    obj = Struct('Histogram')
    Histogram = obj
    obj.attributes.append(Variable('x',HistogramAxis))
    obj.attributes.append(Variable('y',HistogramAxis,optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('x',HistogramAxis,Variable('HistogramAxis()',HistogramAxis)),
            Variable('y',HistogramAxis,None,optional=True),
        ],
        mapping = [
            ('x',[Variable('x')]),
            ('y',[Variable('y')])
        ]
    ))
    objs.append(obj)

    objs.append(CodeBlock(code={
        'cpp': {'''
void from_json(const json &j, std::vector<Histogram> &u) {
    for(auto v: j)
        u.push_back(v);
}
'''
        }
    }))

    obj = Struct ('EvaluationPoint')
    EvaluationPoint = obj
    obj.attributes.append(Variable('state','int'))
    obj.attributes.append(Variable('time','float'))
    obj.attributes.append(Variable('value','float',optional=True))
    obj.attributes.append(Variable('error','float',optional=True))
    obj.attributes.append(Variable('histograms',Histogram,list=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('state_','int',-88),
            Variable('time_','float',nan),
            Variable('value_','float',None,optional=True),
            Variable('error_','float',None,optional=True),
            Variable('histograms_',Histogram,[],list=True),
        ],
        mapping = [
            ('state',[Variable('state_')]),
            ('time',[Variable('time_')]),
            ('value',[Variable('value_')]),
            ('error',[Variable('error_')]),
            ('histograms',[Variable('histograms_')]),
        ]
    ))
    obj.methods.append(Function (
        'GetState',
        'int',
        const = True,
        code = {
            'python':
'''
return self.state
''',
            'cpp':
'''
return state;
''',
            'typescript':
'''
return this.state;
''',
        }
    ))
    obj.methods.append(Function (
        'GetTime',
        'int',
        const = True,
        code = {
            'python':
'''
return self.time
''',
            'cpp':
'''
return time;
''',
            'typescript':
'''
return this.time;
''',
        }
    ))
    obj.methods.append(Function (
        'GetValue',
        'float',
        const = True,
        code = {
            'python':
'''
if self.value is None:
    raise ValueError()
return self.value
''',
            'cpp':
'''
if( not value.has_value() )
    throw std::invalid_argument("value");
return value.value();
''',
            'typescript':
'''
if( this.value === undefined )
    throw new Error("value");
return this.value;
''',
        }
    ))
    obj.methods.append(Function (
        'GetError',
        'float',
        const = True,
        code = {
            'python':
'''
if self.error is None:
    raise ValueError()
return self.error
''',
            'cpp':
'''
if( not error.has_value() )
    throw std::invalid_argument("error");
return error.value();
''',
            'typescript':
'''
if( this.error === undefined )
    throw new Error("error");
return this.error;
''',
        }
    ))
    obj.methods.append(Function (
        'Add',
        EvaluationPoint,
        args = [Variable('histogram',Histogram)],
        code = {
            'python':
'''
self.histograms.append(histogram)
return self
''',
            'cpp':
'''
histograms.push_back(histogram);
return *this;
''',
            'typescript':
'''
this.histograms.push(histogram);
return this;
''',
        }
    ))
    objs.append(obj)

    obj = Struct ('Parameter')
    obj.attributes.append(Variable('value','float'))
    obj.attributes.append(Variable('step','float'))
    obj.attributes.append(Variable('min','float'))
    obj.attributes.append(Variable('max','float'))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('value_','float',nan),
            Variable('step_','float',nan),
            Variable('min_','float',nan),
            Variable('max_','float',nan),
        ],
        mapping = [
            ('value',[Variable('value_')]),
            ('step',[Variable('step_')]),
            ('min',[Variable('min_')]),
            ('max',[Variable('max_')]),
        ]
    ))
    objs.append(obj)

    obj = Struct ('Model')
    Model = obj
    obj.attributes.append(Variable('TimeStart','float'))
    obj.attributes.append(Variable('TimeSteps','int'))
    obj.attributes.append(Variable('NumPaths','int'))
    obj.attributes.append(Variable('updaters',Updater,list=True))
    obj.attributes.append(Variable('evaluations',EvaluationPoint,list=True))
    obj.attributes.append(Variable('RunTimeoutSeconds','float'))
    obj.attributes.append(Variable('MemoryLimitKB','int'))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('TimeStart_','float',nan),
            Variable('TimeSteps_','int',0),
            Variable('NumPaths_','int',0),
            Variable('updaters_',Updater,[],list=True),
            Variable('evaluations_',EvaluationPoint,[],list=True),
            Variable('RunTimeoutSeconds_','float',1),
            Variable('MemoryLimitKB_','int',1),
        ],
        mapping = [
            ('TimeStart',[Variable('TimeStart_')]),
            ('TimeSteps',[Variable('TimeSteps_')]),
            ('NumPaths',[Variable('NumPaths_')]),
            ('updaters',[Variable('updaters_')]),
            ('evaluations',[Variable('evaluations_')]),
            ('RunTimeoutSeconds',[Variable('RunTimeoutSeconds_')]),
            ('MemoryLimitKB',[Variable('MemoryLimitKB_')]),
        ]
    ))

    obj.methods.append(Function (
        'GetNumberOfUpdaters',
        'int',
        const = True,
        code = {
            'python':
'''
return len(self.updaters)
''',
            'cpp':
'''
return updaters.size();
''',
            'typescript':
'''
return this.updaters.length;
''',
            'csharp':
'''
return updaters.Count();
'''
        }
    ))

    obj.methods.append(Function (
        'GetNumberOfStates',
        'int',
        const = True,
        code = {
            'python':
'''
return len([u for u in self.updaters if u.HasState()])
''',
            'cpp':
'''
int n {0};
for(const auto &u: updaters)
    n += u.HasState();
return n;
''',
            'typescript':
'''
return this.updaters.filter(
    u => u.HasState()
).length;
'''
        }
    ))

    obj.methods.append(Function (
        'Add',
        Updater,
        args = [Variable('updater',Updater)],
        code = {
            'python':
'''
self.updaters.append(updater)
updater._equation = self.GetNumberOfUpdaters()-1
updater._state = self.GetNumberOfStates()-1 if updater.HasState() else None
return updater
''',
            'cpp':
'''
updaters.push_back(updater);
auto &u = updaters.back();
u._equation = GetNumberOfUpdaters()-1;
if(u.HasState())
    u._state = GetNumberOfStates()-1;
return u;
''',
            'typescript':
'''
this.updaters.push(updater);
updater._equation = this.GetNumberOfUpdaters()-1;
if(updater.HasState())
    updater._state = this.GetNumberOfStates()-1;
return updater;
''',
        }
    ))

    objs.append(obj)

    obj = Struct('Result')
    Result = obj
    obj.attributes.append(Variable('n','int'))
    obj.attributes.append(Variable('mean','float'))
    obj.attributes.append(Variable('stddev','float'))
    obj.attributes.append(Variable('skewness','float'))

    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('n_','int',0),
            Variable('mean_','float',nan),
            Variable('stddev_','float',nan),
            Variable('skewness_','float',nan),
        ],
        mapping = [
            ('n',[Variable('n_')]),
            ('mean',[Variable('mean_')]),
            ('stddev',[Variable('stddev_')]),
            ('skewness',[Variable('skewness_')]),
        ]
    ))

    obj.methods.append(Function (
        'GetMean',
        'float',
        const = True,
        code = {
            'python':
'''
return self.mean
''',
            'cpp':
'''
return mean;
''',
            'typescript':
'''
return this.mean;
''',
        }
    ))

    obj.methods.append(Function (
        'GetMeanError',
        'float',
        const = True,
        code = {
            'python':
'''
return nan if self.n<=0 else self.stddev/math.sqrt(self.n)
''',
            'cpp':
'''
return n<=0 ? NAN : stddev/std::sqrt(n);
''',
            'typescript':
'''
return this.n<=0 ? Number.NaN : this.stddev/Math.sqrt(this.n);
''',
        }
    ))

    obj.methods.append(Function (
        'GetStdDev',
        'float',
        const = True,
        code = {
            'python':
'''
return self.stddev
''',
            'cpp':
'''
return stddev;
''',
            'typescript':
'''
return this.stddev;
''',
        }
    ))

    obj.methods.append(Function (
        'GetSkewness',
        'float',
        const = True,
        code = {
            'python':
'''
return self.skewness
''',
            'cpp':
'''
return skewness;
''',
            'typescript':
'''
return this.skewness;
''',
        }
    ))

    objs.append(obj)


    obj = Struct('EvaluationResults')
    EvaluationResults = obj
    obj.attributes.append(Variable('names','string',list=True))
    obj.attributes.append(Variable('npaths','int',list=True))
    obj.attributes.append(Variable('mean','float',list=True))
    obj.attributes.append(Variable('stddev','float',list=True))
    obj.attributes.append(Variable('skewness','float',list=True))
    obj.attributes.append(Variable('time_points','float',list=True))
    obj.attributes.append(Variable('time_steps','int',list=True))
    obj.attributes.append(Variable('histograms',Histogram,list=True))
    obj.attributes.append(Variable('model',Model,optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('names_','string',[],list=True),
            Variable('npaths_','int',[],list=True),
            Variable('mean_','float',[],list=True),
            Variable('stddev_','float',[],list=True),
            Variable('skewness_','float',[],list=True),
            Variable('time_points_','float',[],list=True),
            Variable('time_steps_','int',[],list=True),
            Variable('histograms_',Histogram,[],list=True),
            Variable('model_',Model,None,optional=True),
        ],
        mapping = [
            ('names',[Variable('names_')]),
            ('npaths',[Variable('npaths_')]),
            ('mean',[Variable('mean_')]),
            ('stddev',[Variable('stddev_')]),
            ('skewness',[Variable('skewness_')]),
            ('time_points',[Variable('time_points_')]),
            ('time_steps',[Variable('time_steps_')]),
            ('histograms',[Variable('histograms_')]),
            ('model',[Variable('model_')]),
        ]
    ))

    obj.methods.append(Function (
        'NumStates',
        'int',
        const = True,
        code = {
            'python':
'''
return len(self.names)
''',
            'cpp':
'''
return names.size();
''',
            'typescript':
'''
return this.names.length;
''',
        }
    ))

    obj.methods.append(Function (
        'NumEvaluations',
        'int',
        const = True,
        code = {
            'python':
'''
return len(self.time_points)
''',
            'cpp':
'''
return time_points.size();
''',
            'typescript':
'''
return this.time_points.length;
''',
        }
    ))

    obj.methods.append(Function (
        'Index',
        'int',
        args = [
            Variable('state','int'),
            Variable('point','int')
        ],
        const = True,
        code = {
            'python':
'''
if not (state>=0 and state<self.NumStates() and point>=0 and point<self.NumEvaluations()):
    raise ValueError()
return point*self.NumStates() + state
''',
            'cpp':
'''
if( not (state>=0 and state<NumStates() and point>=0 and point<NumEvaluations()) )
    throw std::invalid_argument("Index");
return point*NumStates() + state;
''',
            'typescript':
'''
if( !(state>=0 && state<this.NumStates() && point>=0 && point<this.NumEvaluations()))
    throw new Error(`Index`);
return point*this.NumStates() + state;
''',
        }
    ))

    obj.methods.append(Function (
        'GetStateEvaluationResult',
        Result,
        args = [
            Variable('state','int'),
            Variable('point','int')
        ],
        const = True,
        code = {
            'python':
'''
n = self.Index(state,point)
return Result(self.npaths[n],self.mean[n],self.stddev[n],self.skewness[n])
''',
            'cpp':
'''
auto n = Index(state,point);
return Result(npaths[n],mean[n],stddev[n],skewness[n]);
''',
            'typescript':
'''
const n = this.Index(state,point);
return new Result(this.npaths[n],this.mean[n],this.stddev[n],this.skewness[n]);
''',
        }
    ))

    obj.methods.append(Function (
        'df',
        'any',
        const = True,
        code = {
            'python':
'''
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
''',
        }
    ))

    objs.append(obj)

    for language in languages:
        write_objs(fname,f'{fname}_tests',language,objs)
    
    return objs

if __name__ == '__main__':

    languages = ['python','cpp','typescript']
    objs = create_dto('output/dto',languages)
    for lang1 in languages:
        for lang2 in languages:
            print(f'Testing: {lang1} {lang2}')
            run_round_trip_tests(lang1,lang2,objs,'output')
