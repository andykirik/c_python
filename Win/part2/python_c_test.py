import ctypes 

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


def do_ref_test():
    i = ctypes.c_int()
    d = ctypes.c_double()
    s = ctypes.create_string_buffer(b'\000' * 32)
    f_fill_data(ctypes.byref(i), ctypes.byref(d), s)
    print("Python received int:{0} double:{1} string:{2}".format(i.value, d.value, s.value))

#==============================================================================================================================================#

f_fill_data = wrap_function(clib, "fill_data", None, [ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_char)])

do_ref_test()

#==============================================================================================================================================#
