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

#==============================================================================================================================================#

f_alloc_string = wrap_function(clib, "alloc_C_string", ctypes.POINTER(ctypes.c_char), None)
f_free_string = wrap_function(clib, "free_C_string", None, [ctypes.POINTER(ctypes.c_char)])
f_add_one_to_string = wrap_function(clib, "add_one_to_string", None, [ctypes.POINTER(ctypes.c_char)])

#==============================================================================================================================================#

def run_string_test_1():
    ''' python strings are immutable.  The function adds 1 to each value in the
        array. The python string will remain unchanged afterwards.
        Also try with the ctypes string_buffer which is mutable.
    '''
    print("Calling C function which tries to modify Python string")
    original_string = "starting string"
    print("Before:", original_string)
    # this call does not change value, even though it tries!
    f_add_one_to_string(ctypes.create_string_buffer(str.encode(original_string)))
    print("After: ", original_string)

    # The ctypes string buffer IS mutable, however.
    print("Calling C function with mutable buffer this time")
    # need to encode the original to get bytes for string_buffer
    mutable_string = ctypes.create_string_buffer(str.encode(original_string))
    print("Before:", mutable_string.value)
    f_add_one_to_string(mutable_string)  # works!
    print("After: ", mutable_string.value)

def run_string_test_2():
    ''' Call a C function which allocates memory.  Show how to pass that
        memory pointer back to C to be freed.
    '''
    # set up the C function which returns an allocated string.  The memory for
    # this string is allocated in C and so must be freed in C.
    #
    # I found that having the return type be a simple c_char_p caused a
    # conversion to be done on the return.  If I examined the type of the
    # returned object, it was "bytes" which did not contain the original
    # address of the C memory (at least in any usable form).
    #
    # Using a ctypes.POINTER allows us to preserve that information so we can
    # free it later.

    print("Allocating and freeing memory in C")
    c_string_address = f_alloc_string()
    # now we have the POINTER object.  we should convert that to something we
    # can use on the python side.
    phrase = ctypes.c_char_p.from_buffer(c_string_address)
    print("Python received {0}:{1}".format(hex(ctypes.addressof(c_string_address.contents)), phrase.value))

    # the memory that c_string_address points to was allocated in C, we need to
    # return it there as python's memory manager will NOT free it for us!  This
    # is c_string_address the pointer we have the in c_string_address object is
    # needed.  The POINTER object stores the address of the C memory in the
    # contents attribute.  NOTE: When printing it out, you need the addressof
    # for the contents to tell python NOT to convert it to what the contents
    # pointer is pointing at.
    f_free_string(c_string_address)  # contents is the actual pointer returned

    
#==============================================================================================================================================#

run_string_test_1()
print()
run_string_test_2()
print()

#==============================================================================================================================================#
