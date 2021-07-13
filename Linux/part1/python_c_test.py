import ctypes 

#==============================================================================================================================================#

# Windows
#clib = ctypes.CDLL('./c_lib.dll')
# Unix
clib = ctypes.CDLL('./c_lib.so')

#==============================================================================================================================================#

def wrap_function(lib, funcname, restype, argtypes):
    func = lib.__getattr__(funcname)
    func.restype = restype
    func.argtypes = argtypes
    return func


def run_string_test():
    name = "Andrew" # this is Unicode string
    sw_name = ctypes.c_wchar_p(name) # this is pointer to Unicode string
    res = f_hello(ctypes.create_string_buffer(str.encode(name)))
    phrase = ctypes.c_char_p.from_buffer(res)
    print ("in Python: ", phrase.value)
    f_free_string(res)
    
    name = b"Andy" # this is old NULL terminated string
    s_name = ctypes.c_char_p(name) # this is pointer to old NULL terminated string
    res = f_hello(s_name)
    phrase = ctypes.c_char_p.from_buffer(res)
    print ("in Python: ", phrase.value)
    f_free_string(res)

    
#==============================================================================================================================================#

f_hello = wrap_function(clib, "hello", ctypes.POINTER(ctypes.c_char), [ctypes.POINTER(ctypes.c_char)])
f_free_string = wrap_function(clib, "free_C_string", None, [ctypes.POINTER(ctypes.c_char)])

run_string_test()

#==============================================================================================================================================#
