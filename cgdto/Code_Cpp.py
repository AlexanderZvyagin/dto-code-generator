import os
from .all import *
from .Code import *

class CodeCpp (Code):
    def __init__ (self, options={}):
        super().__init__('cpp','cpp',options)
