import ctypes 
import time
import numpy as np

#==============================================================================================================================================#

# Windows
clib = ctypes.CDLL('./c_lib.dll')
# Unix
#clib = ctypes.CDLL('./c_lib.so')

#==============================================================================================================================================#

def wrap_function(lib, funcname, restype, argtypes):
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func


def run_double_array_test():
    a = np.array([1,2,3], dtype=float)
    b = np.array([4,5,6], dtype=float)
    p_a = a.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    p_b = b.ctypes.data_as(ctypes.POINTER(ctypes.c_double))
    d = ctypes.c_int(len(a))
    c = f_add_vector(p_a, p_b, d)
    for i in range(3):
        print (c[i])
    f_free_memory(c)

#==============================================================================================================================================#

f_add_vector = wrap_function(clib, "add_vector", ctypes.POINTER(ctypes.c_double), [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int])
f_free_memory = wrap_function(clib, "free_mem", None, [ctypes.POINTER(ctypes.c_double)])

run_double_array_test()

#==============================================================================================================================================#
