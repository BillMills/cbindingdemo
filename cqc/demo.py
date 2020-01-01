import ctypes, numpy, os
from numpy.ctypeslib import ndpointer

basedir = os.path.abspath(os.path.dirname(__file__))

libpath = os.path.join(basedir, 'cqc.so')
lib = ctypes.cdll.LoadLibrary(libpath)
fun = lib.cfun
fun.restype = None
fun.argtypes = [ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                ctypes.c_size_t,
                ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
