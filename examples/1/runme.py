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
    obj.attributes.append(Variable('_equation','int'))
    obj.attributes.append(Variable('_state','int'))
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

    obj = Struct('IndependentGaussian',Updater,generate_json=True)
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
    
    obj = Struct('CorrelatedGaussian',Updater,generate_json=True)
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

    obj = Struct('Barrier',Updater,generate_json=True)
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
    obj.attributes.append(Variable('x','HistogramAxis'))
    obj.attributes.append(Variable('y','HistogramAxis'))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('x','HistogramAxis',Variable('HistogramAxis()','type')),
            Variable('y','HistogramAxis',Variable('HistogramAxis()','type')),
        ],
        mapping = [
            ('x',[Variable('x')]),
            ('y',[Variable('y')])
        ]
    ))
    # obj.methods.append(Function (
    #     obj.name,
    #     'constructor',
    #     args = [
    #         Variable('x','HistogramAxis',None),
    #     ],
    #     mapping = [
    #         ('x',[Variable('x')]),
    #     ]
    # ))
    # obj.methods.append(Function (
    #     obj.name,
    #     'constructor',
    #     args = [
    #         Variable('x','HistogramAxis',None),
    #         Variable('y','HistogramAxis',None),
    #     ],
    #     mapping = [
    #         ('x',[Variable('x')]),
    #         ('y',[Variable('y')])
    #     ]
    # ))
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
    obj.attributes.append(Variable('state','int',None))
    obj.attributes.append(Variable('time','float',None))
    obj.attributes.append(Variable('value','float',None))
    obj.attributes.append(Variable('error','float',None))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('state_','int',-88),
            Variable('time_','float',nan),
            Variable('value_','float',nan),
            Variable('error_','float',nan),
        ],
        mapping = [
            ('state',[Variable('state_')]),
            ('time',[Variable('time_')]),
            ('value',[Variable('value_')]),
            ('error',[Variable('error_')]),
        ]
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
    obj.attributes.append(Variable('histograms','Histogram',list=True))
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
    obj.attributes.append(Variable('updaters','Updater',list=True))
    obj.attributes.append(Variable('evaluations','EvaluationPoint',list=True))
    obj.attributes.append(Variable('RunTimeoutSeconds','float'))
    obj.attributes.append(Variable('MemoryLimitKB','int'))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('TimeStart_','float',nan),
            Variable('TimeSteps_','int',0),
            Variable('NumPaths_','int',0),
            Variable('updaters_','Updater',[],list=True),
            Variable('evaluations_','EvaluationPoint',[],list=True),
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
