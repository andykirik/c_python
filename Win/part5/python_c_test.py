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

def get_percent(percent):
    """Print advancement and set the next call when C has advanced a further 20%"""
    print("Advancement of C calculations: %f%%" % (percent*100))
    return percent + 0.2

CB_FTYPE_DOUBLE_DOUBLE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double) # define C pointer to a function type
cb_get_percent = CB_FTYPE_DOUBLE_DOUBLE(get_percent) # define a C function equivalent to the python function "get_percent"
clib.def_python_callback(cb_get_percent)  # call the C code and set a callback

def do_square_using_c(list_in):
    """Call C function to calculate squares"""
    n = len(list_in)
    c_arr_in = (ctypes.c_double * n)(*list_in)
    c_arr_out = (ctypes.c_double * n)()

    clib.c_square(ctypes.c_int(n), c_arr_in, c_arr_out)
    return c_arr_out[:]

def do_square_using_c_with_callback(list_in):
    """Call C function to calculate squares"""
    n = len(list_in)
    c_arr_in = (ctypes.c_double * n)(*list_in)
    c_arr_out = (ctypes.c_double * n)()

    clib.c_square_wcallback(ctypes.c_int(n), c_arr_in, c_arr_out)
    return c_arr_out[:]
  
def run_square_test():
    my_list = np.arange(10)
    squared_list = do_square_using_c(my_list)
    print(squared_list)
    print()
    squared_list = do_square_using_c_with_callback(my_list)
    print(squared_list)
  

#==============================================================================================================================================#

run_square_test()
print()

#==============================================================================================================================================#
