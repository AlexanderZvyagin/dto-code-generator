import os
from .all import *
from .Code import *

class CodeTypescript (Code):
    def __init__ (self, options={}):
        super().__init__('typescript','ts',options)
