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
            Variable('start','float',nan),
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
        'HasState',
        'boolean',
        const = True,
        code = {
            'python':
'''
return self._state>=0
''',
            'cpp':
'''
return _state>=0;
''',
            'typescript':
'''
return this._state>=0;
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

    obj = Struct('EvaluationResults')
    obj.attributes.append(Variable('names','string',list=True))
    obj.attributes.append(Variable('npaths','int',list=True))
    obj.attributes.append(Variable('mean','float',list=True))
    obj.attributes.append(Variable('stddev','float',list=True))
    obj.attributes.append(Variable('skewness','float',list=True))
    obj.attributes.append(Variable('time_points','float',list=True))
    obj.attributes.append(Variable('time_steps','int',list=True))
    obj.attributes.append(Variable('histograms',Histogram,list=True))
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
            Variable('histograms_','Histogram',[],list=True),
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
        ]
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
        'void',
        args = [Variable('updater',Updater)],
        code = {
            'python':
'''
self.updaters.append(updater)
# title = getattr(updater,'_title',None)
# updater._equation = len(self.updaters)-1
# updater._state = self.NumStatefulProcesses()-1 if updater.HasState() else None
# self._titles[updater._state] = title
# return updater
'''
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
