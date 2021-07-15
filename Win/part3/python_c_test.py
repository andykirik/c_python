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

class Point(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    
    def __init__(self, lib, x, y):
        self.show_point_func = wrap_function(lib, 'show_point', None, [Point])
        self.move_point_func = wrap_function(lib, 'move_point', None, [Point])
        self.move_point_ref_func = wrap_function(lib, 'move_point_by_ref', None, [ctypes.POINTER(Point)])
        self.x = x
        self.y = y

    def __repr__(self):
        return '({0}, {1})'.format(self.x, self.y)
    
    def show_point(self):
        self.show_point_func(self)

    def move_point(self):
        self.move_point_func(self)

    def move_point_by_ref(self):
        self.move_point_ref_func(self)

class Line(ctypes.Structure):
    _fields_ = [('start', Point), ('end', Point)]

    def __init__(self, lib, x1, y1, x2, y2):
        self.show_line_func = wrap_function(lib, 'show_line', None, [Line])
        self.move_line_func = wrap_function(lib, 'move_line', None, [ctypes.POINTER(Line)])
        self.start.x = x1
        self.start.y = y1
        self.end.x = x2
        self.end.y = y2

    def __repr__(self):
        return '{0}->{1}'.format(self.start, self.end)

    def move_line(self):
        self.move_line_func(self)

#==============================================================================================================================================#
  
def run_point_test():
    p = Point(clib, 1, 2)
    p.show_point()
    print()

    # --- Pass by value ---
    print("Pass by value")
    a = Point(clib, 5, 6)
    print("Point in Python is", a)
    a.move_point()
    print("Point in Python is", a)
    print()

    # --- Pass by reference ---
    print("Pass by reference")
    a = Point(clib, 5, 6)
    print("Point in Python is", a)
    a.move_point_by_ref()
    print("Point in Python is", a)


#==============================================================================================================================================#

run_point_test()

#==============================================================================================================================================#
