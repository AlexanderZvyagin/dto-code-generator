# This file can be (and should be) imported
# by all language-specific implementations.

import os, subprocess
from collections import namedtuple

indent = ' '*4
autogen_text = 'This is an automatically generated file.'

class Variable:

    def __init__ (
        self,
        name:str = '',
        type     = None,
        defval   = None,
        list     = False,
        optional = False,
        skip_dto = False
    ):
        self.name     = name
        self.type     = type
        self.defval   = defval
        self.list     = list
        self.optional = optional
        self.skip_dto = skip_dto

    def TypeName (self) -> str:
        if isinstance(self.type,Struct):
            return self.type.name
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
    def __init__ (self, name:str, base=None):
        self.name : str = name
        self.attributes : list[Variable] = []
        self.methods : list [Function] = []
        self.base : Struct|None = base
    def __repr__ (self):
        return f"Struct('{self.name}',base={self.base}) #attributes={len(self.attributes)} #methods={len(self.methods)}"
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

    def __init__ (self, name:str, type:str, args=[], code={}, mapping=[], const=False):
        '''code: dictionary of language:str=>list[str]
        
        mapping: it is an array of (key,value) pairs
        '''
        self.name    : str = name
        self.type    : str = type
        self.args    : list[Variable] = args
        self.code    : dict[str, list[str]] = code
        self.mapping : tuple [str,list[Variable]] = mapping
        self.const   : bool = const

    def __repr__ (self):
        return f"Function('{self.name}','{self.type}',{self.args})"

def get_code (body):
    if body is None:
        return []
    elif isinstance(body,str):
        return body.split('\n')
    else:
        return body

def run_test(language,command,struct_name='',file1='',file2=''):
    '''run_test: version 2'''
    cmd = [
        './run',
        command,
        struct_name,
        os.path.abspath(file1) if file1 else '',
        os.path.abspath(file2) if file2 else ''
    ]
    cwd=f'languages/{language}'
    proc = subprocess.run (cmd, capture_output=True, text=True, cwd=cwd)
    if proc.returncode:
        for v in ['stdout','stderr']:
            if not getattr(proc,v):
                continue
            print(f'*** {v} ***')
            print(getattr(proc,v))
    proc.check_returncode()

def run_round_trip_tests(lang1,lang2,objs,outdir):

    for lang in [lang1,lang2]:
        run_test(lang,'build')

    for obj in objs:
        if not isinstance(obj,Struct):
            continue
        struct_name = obj.name
        json_file1 = f'{outdir}/{struct_name}-created-by-{lang1}.json'
        run_test(lang1,'create',struct_name,json_file1)
        json_file2 = f'{outdir}/{struct_name}-created-by-{lang1}-converted-by-{lang2}.json'
        run_test(lang2,'convert',struct_name,json_file1,json_file2) 
        run_test(lang1,'compare',struct_name,json_file1,json_file2)
