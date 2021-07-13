# Specify compiler
CC=g++
 
CFLAGS=-c -Wall -Werror -fpic -I. -std=c++11
LFLAGS= -shared

all: test

clean:
	rm -f *.o *.so

c_lib.so: c_lib.o
	$(CC) $(LFLAGS) -o c_lib.so c_lib.o

c_lib.o: c_lib.cpp
	$(CC) $(CFLAGS) -o c_lib.o c_lib.cpp

test: c_lib.so
	./python_c_test.py

