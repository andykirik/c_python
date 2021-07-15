# Specify compiler
CC=cl.exe
 
# Specify linker
LINK=link.exe

#CFLAGS=-c -Wall -I. /DC_API_EXPORT
CFLAGS=-c -I. /DC_API_EXPORT

#Win32
#LFLAGS= /DLL
#Win64
LFLAGS= /DLL /MACHINE:X64

all: test

clean:
	del *.o *.dll *.exp *.lib

c_lib: c_lib.o
	$(LINK) $(LFLAGS) c_lib.o

c_lib.o: c_lib.cpp c_lib.h
	$(CC) $(CFLAGS) c_lib.cpp /Foc_lib.o

test: c_lib
	 python python_c_test.py

