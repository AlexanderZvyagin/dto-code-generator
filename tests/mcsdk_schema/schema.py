from cgdto import *
from math import nan

def schema_version () -> str:
    return 'MonteCarlo SDK version (0.7.0)'

def V0_Model (Updater,EvaluationPoint):
    obj = Struct ('Model',namespace='V0',default_version=False)
    Model = obj
    obj.AddAttribute(Variable('TimeStart',BasicType.float))
    obj.AddAttribute(Variable('TimeSteps',BasicType.int))
    obj.AddAttribute(Variable('NumPaths',BasicType.int))
    obj.AddAttribute(Variable('updaters',Updater,list=True))
    obj.AddAttribute(Variable('evaluations',EvaluationPoint,list=True))
    obj.AddAttribute(Variable('RandomSeed',BasicType.int,optional=True))
    obj.AddAttribute(Variable('RunTimeoutSeconds',BasicType.float,optional=True))
    obj.AddAttribute(Variable('MemoryLimitKB',BasicType.int,optional=True))
    obj.AddAttribute(Variable('titles','dict[int,string]',skip_dto=True))
    obj.AddAttribute(Variable('_nstates',BasicType.int,skip_dto=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('TimeStart',BasicType.float,nan),
            Variable('TimeSteps',BasicType.int,0),
            Variable('NumPaths',BasicType.int,0),
            Variable('updaters',Updater,[],list=True),
            Variable('evaluations',EvaluationPoint,[],list=True),
            Variable('RandomSeed',BasicType.int,None,optional=True),
            Variable('RunTimeoutSeconds',BasicType.float,None,optional=True),
            Variable('MemoryLimitKB',BasicType.int,None,optional=True),
            Variable('nstates',BasicType.int,0),
        ],
        mapping = [
            ('TimeStart'        ,[Variable('TimeStart')]),
            ('TimeSteps'        ,[Variable('TimeSteps')]),
            ('NumPaths'         ,[Variable('NumPaths')]),
            ('updaters'         ,[Variable('updaters')]),
            ('evaluations'      ,[Variable('evaluations')]),
            ('RandomSeed'       ,[Variable('RandomSeed')]),
            ('RunTimeoutSeconds',[Variable('RunTimeoutSeconds')]),
            ('MemoryLimitKB'    ,[Variable('MemoryLimitKB')]),
            ('_nstates'         ,[Variable('nstates')]),
        ],
        code = {
            'python':
'''
self.titles = {}
''',
            'typescript':
'''
this.titles = {};
'''
        }
    ))

    obj.methods.append(Function (
        '__repr__',
        BasicType.string,
        const = True,
        code = {
            'python':
'''
return f'TimeStart={self.TimeStart} TimeSteps={self.TimeSteps} NumPaths={self.NumPaths} updaters={len(self.updaters)}'
'''
        }
    ))

    obj.methods.append(Function (
        'GetNumberOfUpdaters',
        BasicType.int,
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
        BasicType.int,
        const = True,
        code = {
            'python':
'''
return self._nstates
''',
            'cpp':
'''
return _nstates;
''',
            'typescript':
'''
return this._nstates;
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
updater._state = self._nstates
self._nstates += updater._nstates
self.updaters.append(updater)
self.titles[updater._state] = updater.title
return updater
''',
            'cpp':
'''
updaters.push_back(updater);
auto &u = updaters.back();
u._state = _nstates;
_nstates += updater._nstates;
titles[u._state] = u.title;
return u;
''',
            'typescript':
'''
updater._state = this._nstates;
this._nstates += updater._nstates;
this.updaters.push(updater);
this.titles[updater._state] = updater.title;
return updater;
''',
        }
    ))

    return obj
    

def V1_Model (Updater,EvaluationPoint):
    version = 1
    obj = Struct ('Model',namespace=f'V{version}',default_version=True)
    Model = obj
    obj.AddAttribute(Variable('version',BasicType.string,defval=f'{obj.name}:{version}'))
    obj.AddAttribute(Variable('TimeStart',BasicType.float))
    obj.AddAttribute(Variable('TimeSteps',BasicType.int))
    obj.AddAttribute(Variable('NumPaths',BasicType.int))
    obj.AddAttribute(Variable('updaters',Updater,list=True))
    obj.AddAttribute(Variable('evaluations',EvaluationPoint,list=True))
    obj.AddAttribute(Variable('RandomSeed',BasicType.int,optional=True))
    obj.AddAttribute(Variable('RunTimeoutSeconds',BasicType.float,optional=True))
    obj.AddAttribute(Variable('titles','dict[int,string]',skip_dto=True))
    obj.AddAttribute(Variable('_nstates',BasicType.int,skip_dto=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('TimeStart',BasicType.float,nan),
            Variable('TimeSteps',BasicType.int,0),
            Variable('NumPaths',BasicType.int,0),
            Variable('updaters',Updater,[],list=True),
            Variable('evaluations',EvaluationPoint,[],list=True),
            Variable('RandomSeed',BasicType.int,None,optional=True),
            Variable('RunTimeoutSeconds',BasicType.float,None,optional=True),
            Variable('nstates',BasicType.int,0),
        ],
        mapping = [
            ('TimeStart'        ,[Variable('TimeStart')]),
            ('TimeSteps'        ,[Variable('TimeSteps')]),
            ('NumPaths'         ,[Variable('NumPaths')]),
            ('updaters'         ,[Variable('updaters')]),
            ('evaluations'      ,[Variable('evaluations')]),
            ('RandomSeed'       ,[Variable('RandomSeed')]),
            ('RunTimeoutSeconds',[Variable('RunTimeoutSeconds')]),
            ('_nstates'         ,[Variable('nstates')]),
        ],
        code = {
            'python':
'''
self.titles = {}
''',
            'typescript':
'''
this.titles = {};
'''
        }
    ))

    obj.methods.append(Function (
        '__repr__',
        BasicType.string,
        const = True,
        code = {
            'python':
'''
return f'TimeStart={self.TimeStart} TimeSteps={self.TimeSteps} NumPaths={self.NumPaths} updaters={len(self.updaters)}'
'''
        }
    ))

    obj.methods.append(Function (
        'GetNumberOfUpdaters',
        BasicType.int,
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
        BasicType.int,
        const = True,
        code = {
            'python':
'''
return self._nstates
''',
            'cpp':
'''
return _nstates;
''',
            'typescript':
'''
return this._nstates;
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
updater._state = self._nstates
self._nstates += updater._nstates
self.updaters.append(updater)
self.titles[updater._state] = updater.title
return updater
''',
            'cpp':
'''
updaters.push_back(updater);
auto &u = updaters.back();
u._state = _nstates;
_nstates += updater._nstates;
titles[u._state] = u.title;
return u;
''',
            'typescript':
'''
updater._state = this._nstates;
this._nstates += updater._nstates;
this.updaters.push(updater);
this.titles[updater._state] = updater.title;
return updater;
''',
        }
    ))

    return obj

def add(funcs=[],kargs=(),kwargs={}):
    objs = []
    default_obj = None
    for func in funcs:
        obj = func(*kargs,**kwargs)
        objs.append(obj)
        if obj.default_version:
            assert default_obj is None
            default_obj = obj
    return objs, default_obj

def schema ():

    objs = [] # objects in the file

    obj = Struct('Error')
    Error = obj
    obj.AddAttribute(Variable('message',BasicType.string, optional=True))
    obj.AddAttribute(Variable('details',BasicType.string, optional=True))
    obj.AddAttribute(Variable('code',BasicType.int, optional=True))
    obj.AddAttribute(Variable('errors',Error, optional=True, list=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('message',BasicType.string,optional=True,defval=None),
            Variable('details',BasicType.string,optional=True,defval=None),
            Variable('code',BasicType.int,optional=True,defval=None),
            Variable('errors',Error,optional=True,list=True,defval=None),
        ],
        mapping = [
            ('message',[Variable('message')]),
            ('details',[Variable('details')]),
            ('code',[Variable('code')]),
            ('errors',[Variable('errors')]),
        ]
    ))
    objs.append(obj)

    obj = Struct('UpdaterDoc')
    obj.AddAttribute(Variable('name',BasicType.string,doc='''
The parameter 'name' is a single world which uniquely identifies how a MC state will be updated.
E.g. GeometricalBrownianMotion.
'''))
    obj.AddAttribute(Variable('title',BasicType.string,doc='Short description (single line) what the updater is doing.'))
    obj.AddAttribute(Variable('doc_md',BasicType.string,doc='Long multiline description of the updater using Markdown format.'))
    obj.AddAttribute(Variable('start',BasicType.string))
    obj.AddAttribute(Variable('nargs_min',BasicType.int))
    obj.AddAttribute(Variable('nrefs_min',BasicType.int))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name',BasicType.string,''),
            Variable('title',BasicType.string,''),
            Variable('doc_md',BasicType.string,''),
            Variable('start',BasicType.string,''),
            Variable('nargs_min',BasicType.int,-88),
            Variable('nrefs_min',BasicType.int,-88)
        ],
        mapping = [
            ('name',[Variable('name')]),
            ('title',[Variable('title')]),
            ('doc_md',[Variable('doc_md')]),
            ('start',[Variable('start')]),
            ('nargs_min',[Variable('nargs_min')]),
            ('nrefs_min',[Variable('nrefs_min')]),
        ]
    ))
    objs.append(obj)

    obj = Struct('UpdaterDto',doc='''
UpdaterDto is used to pass parameters to update a state.
''')
    objs.append(obj)
    UpdaterDto = obj
    obj.AddAttribute(Variable('name',BasicType.string))
    obj.AddAttribute(Variable('refs',BasicType.int, list=True, optional=True))
    obj.AddAttribute(Variable('args',BasicType.float, list=True, optional=True))
    obj.AddAttribute(Variable('start',BasicType.float,list=True, optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name', BasicType.string, '',doc='Unique name of the updater, e.g. BrownianMotion'),
            Variable(name='refs', type=BasicType.int, defval=None, list=True, optional=True, doc='List of states which an updater requires.'),
            Variable('args', BasicType.float, defval=None, list=True, optional=True, doc='List of arguments.'),
            Variable('start', BasicType.float, defval=None, list=True, optional=True, doc='State starting value, e.g. start=3 will start a BM process from value 3.')
        ],
        mapping = [
            ('name',[Variable('name')]),
            ('refs',[Variable('refs')]),
            ('args',[Variable('args')]),
            ('start',[Variable('start')]),
        ]
    ))

    obj = Struct('Updater',UpdaterDto)
    objs.append(obj)
    Updater = obj
    obj.AddAttribute(Variable('_state',BasicType.int,skip_dto=True))
    obj.AddAttribute(Variable('_nstates',BasicType.int,skip_dto=True))
    obj.AddAttribute(Variable('title',BasicType.string,skip_dto=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('name',BasicType.string,''),
            Variable('refs',BasicType.int,[],list=True),
            Variable('args',BasicType.float,[],list=True),
            Variable('start',BasicType.float,[],list=True),
            Variable('nstates',BasicType.int,1),
            Variable('title',BasicType.string,''),
        ],
        mapping = [
            (obj.base.name,[
                Variable('name'),
                Variable('refs'),
                Variable('args'),
                Variable('start'),
            ]),
            ('_state',[-88]),
            ('_nstates',[Variable('nstates')]),
            ('title',[Variable('title')]),
        ]
    ))

    obj.methods.append(Function (
        '__repr__',
        BasicType.string,
        const = True,
        code = {
            'python':
'''
if self._nstates==0:
    state='None'
elif self._nstates==1:
    state=f'{self._state}'
else:
    states=f'[{self._state}...{self._state+self._nstates-1}]'
refs = str(self.refs)
args = str(self.args)
return f'{self.name} nstates={self._nstates} state={self._state} refs={self.refs} args={self.args} start={self.start}'
'''
        }
    ))
    
    obj.methods.append(Function (
        'GetStateNumber',
        BasicType.int,
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
        'GetStart',
        Variable(None,BasicType.float, list=True),
        const = True,
        code = {
            'python':
'''
return []   if self.start is None else   self.start
''',
            'cpp':
'''
return start.value_or(std::vector<float>{});
''',
            'typescript':
'''
return this.start || [];
'''
        }
    ))

    objs.append(CodeBlock(code={
        'cpp': {'''
void from_json(const json &j, std::vector<Updater> &u) {
    for(auto v: j)
        u.push_back(v);
}
'''
        }
    }))

    obj = Struct('BrownianMotion',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start'     ,BasicType.float, nan),
            Variable('drift'     ,BasicType.float, nan),
            Variable('diffusion' ,BasicType.float, nan),
            Variable('title'     ,BasicType.string,''),
        ],
        mapping = [(obj.base.name,[
            'BrownianMotion',
            [], # refs
            [Variable('drift'),Variable('diffusion')], # args
            [Variable('start')],
            1,
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('BrownianMotionRef',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start'     ,BasicType.float, nan),
            Variable('drift'     ,BasicType.int  , -88),
            Variable('diffusion' ,BasicType.int  , -88),
            Variable('title'     ,BasicType.string,''),
        ],
        mapping = [(obj.base.name,[
            'BrownianMotion',
            [Variable('drift'),Variable('diffusion')], # refs
            [], # args
            [Variable('start')],
            1,
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('GeometricalBrownianMotion',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start'     ,BasicType.float, nan),
            Variable('drift'     ,BasicType.float, nan),
            Variable('diffusion' ,BasicType.float, nan),
            Variable('title'     ,BasicType.string,''),
        ],
        mapping = [(obj.base.name,[
            'GeometricalBrownianMotion',
            [], # refs
            [Variable('drift'),Variable('diffusion')], # args
            [Variable('start')],
            1,
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('GeometricalBrownianMotionRef',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('start'     ,BasicType.float, nan),
            Variable('drift'     ,BasicType.int  , -88),
            Variable('diffusion' ,BasicType.int  , -88),
            Variable('title'     ,BasicType.string,''),
        ],
        mapping = [(obj.base.name,[
            'GeometricalBrownianMotion',
            [Variable('drift'),Variable('diffusion')], # refs
            [], # args
            [Variable('start')],
            1,
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('ZeroCouponBond',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('underlying',BasicType.int  , -88),
            Variable('start'     ,BasicType.float, nan),
            Variable('title'     ,BasicType.string,''),
        ],
        mapping = [(obj.base.name,[
            'ZeroCouponBond',
            [Variable('underlying')], # refs
            [], # args
            [Variable('start')],
            1,
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('Option',Updater)
    obj.AddAttribute(Variable('Call',BasicType.int,defval=0, static=True, skip_dto=True))
    obj.AddAttribute(Variable('Put' ,BasicType.int,defval=1, static=True, skip_dto=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('underlying',BasicType.int  , -88),
            Variable('strike'    ,BasicType.float, nan),
            Variable('call_put'  ,BasicType.int,   -88),
            Variable('title'     ,BasicType.string,''),
        ],
        mapping = [(obj.base.name,[
            'Option',
            [Variable('underlying')], # refs
            [Variable('strike'),Variable('call_put')], # args
            [], # start
            1,
            Variable('title'),
        ])]
    ))
    objs.append(obj)

    obj = Struct('Barrier',Updater)
    obj.AddAttribute(Variable('DirectionUp',BasicType.int,defval=1, static=True, skip_dto=True))
    obj.AddAttribute(Variable('DirectionDown',BasicType.int,defval=-1, static=True, skip_dto=True))
    obj.AddAttribute(Variable('DirectionAny',BasicType.int,defval=0, static=True, skip_dto=True))
    obj.AddAttribute(Variable('ActionSet',BasicType.int,defval=0, static=True, skip_dto=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('underlying',BasicType.int  ,-88),
            Variable('start'     ,BasicType.float,nan),
            Variable('level'     ,BasicType.float,nan),
            Variable('direction' ,BasicType.int  ,-88),
            Variable('action'    ,BasicType.int  ,-88),
            Variable('value'     ,BasicType.float,nan),
            Variable('title'     ,BasicType.string,''),
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
            [Variable('start')],
            1,
            Variable('title'),
        ])]
    ))

    objs.append(obj)


    obj = Struct('Polynom',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('ref'     ,BasicType.int,defval=-1),
            Variable('args'    ,BasicType.float,defval=[],list=True),
            Variable('title'   ,BasicType.string,defval=''),
        ],
        mapping = [(obj.base.name,[
            'Polynom',
            [Variable('ref')],
            Variable('args'),
            [], # start
            1,
            Variable('title'),
        ])]
    ))
    objs.append(obj)


    obj = Struct('Linear1DInterpolation',Updater,gen_test=False)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('ref'    ,BasicType.int   ,defval=-88),
            Variable('xmin'   ,BasicType.float ,defval=-1),
            Variable('xmax'   ,BasicType.float ,defval=1),
            Variable('y'      ,BasicType.float ,defval=[],list=True),
            Variable('title'  ,BasicType.string,defval=''),
        ],
        mapping = [(obj.base.name,[
            'Linear1DInterpolation',
            [Variable('ref')],
            [], # args
            [], # start
            1,
            Variable('title'),
        ])],
        code = {
            'cpp' : '''
if(y.size()<2)
    throw std::invalid_argument("Linear1DInterpolation: y-vector must have at least 2 elements: y(xmin), y(xmax)");
args.value() = std::vector<float>();
args.value().reserve(2+y.size());
args.value().push_back(xmin);
args.value().push_back(xmax);
for(auto item: y)
    args.value().push_back(item);
''',
            'python' : '''
if len(y)<2:
    raise ValueError("Linear1DInterpolation: y-vector must have at least 2 elements: y(xmin), y(xmax)")
self.args = [xmin,xmax] + y
''',
            'typescript' : '''
if(y.length<2)
    throw new Error("Linear1DInterpolation: y-vector must have at least 2 elements: y(xmin), y(xmax)");
this.args = [...[xmin,xmax],...y];
''',
        }
    ))
    objs.append(obj)


    obj = Struct('Multiplication',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('refs'     ,BasicType.int,defval=[],list=True),
            Variable('factor'   ,BasicType.float,defval=1),
            Variable('title'     ,BasicType.string,defval=''),
        ],
        mapping = [(obj.base.name,[
            'Multiplication',
            Variable('refs'),
            [Variable('factor')],
            [], # start
            1,
            Variable('title'),
        ])]
    ))
    objs.append(obj)


    obj = Struct('Division',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('numerator'     ,BasicType.int,defval=-88),
            Variable('denominator'   ,BasicType.int,defval=-88),
            Variable('eps'           ,BasicType.float,defval=0),
            Variable('title'         ,BasicType.string,defval=''),
        ],
        mapping = [(obj.base.name,[
            'Division',
            [Variable('numerator'),Variable('denominator')],
            [Variable('eps')],
            [], # start
            1,
            Variable('title'),
        ])]
    ))
    objs.append(obj)


    obj = Struct('HistogramAxis')
    HistogramAxis = obj
    obj.AddAttribute(Variable('state',BasicType.int))
    obj.AddAttribute(Variable('nbins',BasicType.int))
    obj.AddAttribute(Variable('min',BasicType.float,optional=True))
    obj.AddAttribute(Variable('max',BasicType.float,optional=True))
    obj.AddAttribute(Variable('title',BasicType.string,optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('state',BasicType.int,-88),
            Variable('nbins',BasicType.int,-88),
            Variable('min'  ,BasicType.float,-88), # FIXME: cannot use math.nan for the moment
            Variable('max'  ,BasicType.float,-88), # FIXME: cannot use math.nan for the moment
            Variable('title'  ,BasicType.string,''), # FIXME: cannot use math.nan for the moment
        ],
        mapping = [
            ('state',[Variable('state')]),
            ('nbins',[Variable('nbins')]),
            ('min',  [Variable('min'  )]),
            ('max',  [Variable('max'  )]),
            ('title',[Variable('title')]),
        ]
    ))
    objs.append(obj)

    obj = Struct('Histogram')
    Histogram = obj
    obj.AddAttribute(Variable('ax',HistogramAxis))
    obj.AddAttribute(Variable('ay',HistogramAxis,optional=True))
    obj.AddAttribute(Variable('evaluation_point',BasicType.int,optional=True))
    obj.AddAttribute(Variable('bins',BasicType.float,list=True,optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('ax',HistogramAxis,Variable('HistogramAxis()',HistogramAxis)),
            Variable('ay',HistogramAxis,None,optional=True),
            Variable('evaluation_point',BasicType.int,None,optional=True),
            Variable('bins',BasicType.float,None,optional=True,list=True)
        ],
        mapping = [
            ('ax',[Variable('ax')]),
            ('ay',[Variable('ay')]),
            ('evaluation_point',[Variable('evaluation_point')]),
            ('bins',[Variable('bins')]),
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


        # Type            =  0,
        # Flags           =  1,
        
        # ExtractionPoint =  2,
        # TimeStep        =  3,

        # Xstate          =  4,
        # Xbins           =  5,
        # Xmin            =  6,
        # Xmax            =  7,

        # Ystate          =  8,
        # Ybins           =  9,
        # Ymin            = 10,
        # Ymax            = 11,

        # Zstate          = 12,
        # Zbins           = 13,
        # Zmin            = 14,
        # Zmax            = 15,

        # TitleBegin      = 16,
        # TitleEnd        = 32,
        # TitleMaxLength  = (TitleEnd-TitleBegin)*sizeof(float)-1, // c-style string! Remember about the trailing 0.

        # DataStart       = TitleEnd



    obj = Struct('Histogram2')
    Histogram2 = obj
    obj.AddAttribute(Variable('AxisX',HistogramAxis))
    obj.AddAttribute(Variable('AxisY',HistogramAxis,optional=True))
    obj.AddAttribute(Variable('AxisZ',HistogramAxis,optional=True))
    obj.AddAttribute(Variable('Flags',BasicType.int,optional=True))
    obj.AddAttribute(Variable('EvaluationPoint',BasicType.int,optional=True))
    obj.AddAttribute(Variable('TimeStep',BasicType.int,optional=True))
    obj.AddAttribute(Variable('Title',BasicType.string,optional=True))
    obj.AddAttribute(Variable('Bins',BasicType.float,list=True,optional=True))

    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('AxisX',HistogramAxis,defval=Variable('HistogramAxis()',HistogramAxis)),
            Variable('AxisY',HistogramAxis,optional=True),
            Variable('AxisZ',HistogramAxis,optional=True),
            Variable('Flags',BasicType.int,optional=True),
            Variable('EvaluationPoint',BasicType.int,optional=True),
            Variable('TimeStep',BasicType.int,optional=True),
            Variable('Title',BasicType.string,optional=True),
            Variable('Bins',BasicType.float,optional=True,list=True),
        ],
        mapping = [
            ('AxisX',[Variable('AxisX')]),
            ('AxisY',[Variable('AxisY')]),
            ('AxisZ',[Variable('AxisZ')]),
            ('Flags',[Variable('Flags')]),
            ('EvaluationPoint',[Variable('EvaluationPoint')]),
            ('TimeStep',[Variable('TimeStep')]),
            ('Title',[Variable('Title')]),
            ('Bins',[Variable('Bins')]),
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
    obj.AddAttribute(Variable('time',BasicType.float))
    obj.AddAttribute(Variable('histograms',Histogram,list=True,optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('time',BasicType.float,nan),
            Variable('histograms',Histogram,None,optional=True,list=True),
        ],
        mapping = [
            ('time',[Variable('time')]),
            ('histograms',[Variable('histograms')]),
        ]
    ))
    obj.methods.append(Function (
        'GetTime',
        BasicType.int,
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
        'Add',
        EvaluationPoint,
        args = [Variable('histogram',Histogram)],
        code = {
            'python':
'''
if getattr(self,'histograms',None) is None:
    self.histograms = []
self.histograms.append(histogram)
return self
''',
            'cpp':
'''
if( not histograms.has_value() )
    histograms = std::vector<Histogram> ();
histograms.value().push_back(histogram);
return *this;
''',
            'typescript':
'''
if(this.histograms === undefined)
    this.histograms = [];
this.histograms.push(histogram);
return this;
''',
        }
    ))

    objs.append(obj)

    Model_versions, Model = add([V0_Model,V1_Model],kargs=(Updater,EvaluationPoint))
    # Model_versions, Model = Model_schema(Updater,EvaluationPoint)
    objs.extend(Model_versions)

    obj = Struct('Result')
    Result = obj
    obj.AddAttribute(Variable('n',BasicType.int))
    obj.AddAttribute(Variable('mean',BasicType.float))
    obj.AddAttribute(Variable('stddev',BasicType.float))
    obj.AddAttribute(Variable('skewness',BasicType.float))

    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('n',BasicType.int,0),
            Variable('mean',BasicType.float,nan),
            Variable('stddev',BasicType.float,nan),
            Variable('skewness',BasicType.float,nan),
        ],
        mapping = [
            ('n',[Variable('n')]),
            ('mean',[Variable('mean')]),
            ('stddev',[Variable('stddev')]),
            ('skewness',[Variable('skewness')]),
        ]
    ))

    obj.methods.append(Function (
        'GetMean',
        BasicType.float,
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
        BasicType.float,
        const = True,
        doc = 'The function computes an error estimate of the mean value.',
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
        BasicType.float,
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
        BasicType.float,
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
    EvaluationResults.AddDependency(Result)
    obj.AddAttribute(Variable('names',BasicType.string,list=True))
    obj.AddAttribute(Variable('npaths',BasicType.int,list=True))
    obj.AddAttribute(Variable('mean',BasicType.float,list=True))
    obj.AddAttribute(Variable('stddev',BasicType.float,list=True))
    obj.AddAttribute(Variable('skewness',BasicType.float,list=True))
    obj.AddAttribute(Variable('time_points',BasicType.float,list=True))
    obj.AddAttribute(Variable('time_steps',BasicType.int,list=True))
    obj.AddAttribute(Variable('histograms',Histogram,list=True))
    obj.AddAttribute(Variable('histograms2',Histogram2,list=True))
    obj.AddAttribute(Variable('model',Model,optional=True))
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('names',BasicType.string,[],list=True),
            Variable('npaths',BasicType.int,[],list=True),
            Variable('mean',BasicType.float,[],list=True),
            Variable('stddev',BasicType.float,[],list=True),
            Variable('skewness',BasicType.float,[],list=True),
            Variable('time_points',BasicType.float,[],list=True),
            Variable('time_steps',BasicType.int,[],list=True),
            Variable('histograms',Histogram,[],list=True),
            Variable('histograms2',Histogram2,[],list=True),
            Variable('model',Model,None,optional=True),
        ],
        mapping = [
            ('names',[Variable('names')]),
            ('npaths',[Variable('npaths')]),
            ('mean',[Variable('mean')]),
            ('stddev',[Variable('stddev')]),
            ('skewness',[Variable('skewness')]),
            ('time_points',[Variable('time_points')]),
            ('time_steps',[Variable('time_steps')]),
            ('histograms',[Variable('histograms')]),
            ('histograms2',[Variable('histograms2')]),
            ('model',[Variable('model')]),
        ]
    ))

    obj.methods.append(Function (
        'GetNumberOfStates',
        BasicType.int,
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
        'GetNumberOfEvaluations',
        BasicType.int,
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
        BasicType.int,
        args = [
            Variable('state',BasicType.int),
            Variable('point',BasicType.int)
        ],
        const = True,
        code = {
            'python':
'''
if not (state>=0 and state<self.GetNumberOfStates() and point>=0 and point<self.GetNumberOfEvaluations()):
    raise ValueError()
return point*self.GetNumberOfStates() + state
''',
            'cpp':
'''
if( not (state>=0 and state<GetNumberOfStates() and point>=0 and point<GetNumberOfEvaluations()) )
    throw std::invalid_argument("Index");
return point*GetNumberOfStates() + state;
''',
            'typescript':
'''
if( !(state>=0 && state<this.GetNumberOfStates() && point>=0 && point<this.GetNumberOfEvaluations()))
    throw new Error(`Index`);
return point*this.GetNumberOfStates() + state;
''',
        }
    ))

    obj.methods.append(Function (
        'GetStateEvaluationResult',
        Result,
        args = [
            Variable('state',BasicType.int),
            Variable('point',BasicType.int)
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
for j in range(self.GetNumberOfEvaluations()):
    for i in range(self.GetNumberOfStates()):
        n = self.Index(i,j)
        item = {
            'name': self.names[i],
            'title': '',
            'state': i,
            'point': j,
            'time': self.time_points[j],
            'step': self.time_steps[j],
            'npaths': self.npaths[n],
            'mean':self.mean[n],
            'mean_error': None if (self.stddev[n] is None or self.npaths[n]<=0) else self.stddev[n]/math.sqrt(self.npaths[n]),
            'stddev': self.stddev[n],
            'skewness': self.skewness[n]
        }
        if self.model:
            item['title'] = self.model.titles.get(i,'')
        data.append(item)
return pd.DataFrame(data)
''',
            'cpp': None,
            'typescript': None,
        }
    ))

    objs.append(obj)

    objs.append(CodeBlock(code={
        'python': {'''
def EvaluationResults_from_response(r,model=None):
    er = EvaluationResults_from_json_string(r.text)
    er.model = model
    return er
'''
        }
    }))

    obj = Struct('Sum',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('weights'  , BasicType.float  , defval=[], list=True),
            Variable('states'   , BasicType.int    , defval=[], list=True),
            Variable('title'    , BasicType.string , defval=''),
        ],
        mapping = [(obj.base.name,[
            'Sum',
            Variable('states'),
            Variable('weights'),
            [],
            1,
            Variable('title'),
        ])],
    ))
    objs.append(obj)

    obj = Struct('SumOfFutureValues',Updater)
    obj.methods.append(Function (
        obj.name,
        'constructor',
        args = [
            Variable('state' , BasicType.int    , defval=-88),
            Variable('t'     , BasicType.float  , defval=[], list=True),
            Variable('title' , BasicType.string , defval=''),
        ],
        mapping = [(obj.base.name,[
            'SumOfFutureValues',
            [Variable('state')],
            Variable('t'),
            [],
            1,
            Variable('title'),
        ])],
    ))
    objs.append(obj)

    objs.append(Include({
        'python'    : ['include.py'],
        'typescript': ['include.ts']
    }))

    return objs
