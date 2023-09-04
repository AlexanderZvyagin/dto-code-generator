# This file can be (and should be) imported
# by all language-specific implementations.

from __future__ import annotations
import os, subprocess, re
from collections import namedtuple

__version__ = (0,6,3)

def version() -> str:
    return f'{__version__[0]}.{__version__[1]}.{__version__[2]}'

indent = ' '*4
def autogen_text (schema = None):
    txt = f'''
https://github.com/AlexanderZvyagin/dto-code-generator
Generated by CODE GENERATOR OF DATA TRANSFER OBJECTS (cgdto) version {version()}
'''
    if schema:
        txt += f'''
Generated from schema: {schema}
'''

    return txt

def detect_dict_key_value (name):
    q = re.match('dict\[(.*),(.*)\]',name)
    return q.groups() if q else None

class Variable:

    def __init__ (
        self,
        name:str = '',
        type     = None,
        defval   = None,
        list     = False,
        optional = False,
        skip_dto = False,
        static   = False
    ):
        self.name     = name
        self.type     = type
        self.defval   = defval
        self.list     = list
        self.optional = optional
        self.skip_dto = skip_dto
        self.static   = static

    def TypeName (self) -> str:
        if isinstance(self.type,Struct):
            return self.type.name
        elif isinstance(self.type,Variable):
            self.type.TypeName()
            return self.type.TypeName()
        else:
            assert isinstance(self.type,str)
            return self.type

    def __repr__ (self):
        return f'Variable(name={self.name},type={self.type},defval={self.defval},list={self.list},optional={self.optional},skip_dto={self.skip_dto})'

ext = {
    'cpp'           : 'cpp',
    'python'        : 'py',
    'typescript'    : 'ts',
    'csharp'        : 'cs',
}

class Struct:
    '''Holds info on a structure.

    Should contain info enough to generate code for all languages.
    '''

    def __init__ (
        self,
        name:str,
        base = None,
        gen_test: bool = True
    ):
        self.name         : str             = name
        self.attributes   : list [Variable] = []
        self.methods      : list [Function] = []
        self.base         : Struct|None     = base
        self.gen_test     : bool            = gen_test
        self.dependencies : list[Struct]    = [base] if base else []

    def __repr__ (self):
        return f"Struct('{self.name}',base={self.base}) #attributes={len(self.attributes)} #methods={len(self.methods)}"

    def AddDependency (self, dep:Struct):
        assert isinstance(dep,Struct)
        if not dep in self.dependencies:
            self.dependencies.append(dep)

    def AddAttribute (self,attr):
        assert isinstance(attr,Variable)
        self.attributes.append(attr)
        if isinstance(attr.type,Struct) and attr.type.name!=self.name:
            self.AddDependency(attr.type)

    def GetAllAttributes (self):
        attrs = []
        this = self
        while this:
            attrs = [a for a in this.attributes] + attrs
            this = this.base
        return attrs

class CodeBlock:
    def __init__ (self, code={}):
        self.code = code

class Function:

    def __init__ (
        self,
        name: str,
        type: str,
        args = [],
        code: dict[str,list[str]] = {},
        mapping = [],
        const: bool=False
    ):
        '''code: dictionary of language:str=>list[str]

        mapping: it is an array of (key,value) pairs
        '''
        self.name        : str = name
        self.type        : str = type
        self.args        : list[Variable] = args
        self.code        : dict[str, list[str]] = code
        self.mapping     : tuple [str,list[Variable]] = mapping
        self.const       : bool = const

    def __repr__ (self):
        return f"Function('{self.name}','{self.type}',{self.args})"

class Include:

    def __init__ (self,files: dict[str,list[str]]):
        self.files = files

def get_code (body):
    if body is None:
        return []
    elif isinstance(body,str):
        return body.split('\n')
    else:
        return body

def run_test(outdir,command,struct_name='',file1='',file2=''):
    '''run_test: version 2'''
    cmd = [
        './run',
        command,
        struct_name,
        os.path.abspath(file1) if file1 else '',
        os.path.abspath(file2) if file2 else ''
    ]
    proc = subprocess.run (cmd, capture_output=True, text=True, cwd=outdir)
    if proc.returncode:
        for v in ['stdout','stderr']:
            if not getattr(proc,v):
                continue
            print(f'*** {v} ***')
            print(getattr(proc,v))
            print(f'**************')
    proc.check_returncode()

supported_languages = {}
def register (Code_class):
    supported_languages[Code_class().language] = Code_class
