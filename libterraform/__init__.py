import os
import platform
from ctypes import cdll, c_void_p

__version__ = '0.2.0'

root = os.path.dirname(os.path.abspath(__file__))
_lib_filename = 'libterraform.dll' if platform.system() == 'Windows' else 'libterraform.so'
_lib_tf = cdll.LoadLibrary(os.path.join(root, _lib_filename))

_free = _lib_tf.Free
_free.argtypes = [c_void_p]

from .cli import TerraformCommand
from .config import TerraformConfig

__all__ = ['TerraformCommand', 'TerraformConfig']