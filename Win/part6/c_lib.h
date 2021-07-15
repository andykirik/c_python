#pragma once

#include "export.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern "C"
{
	typedef double give_and_take_double(double p); // type definition
	give_and_take_double* tell_python;             // pointer to a function of type "give_and_take_double"

	C_SDK_EXPORTED void def_python_callback(give_and_take_double* func)
	{
		// Function called by Python once
		// Defines what "tell_python" is pointing to
		tell_python = func;
	}

	//return the square of array_in of length n in array_out
	C_SDK_EXPORTED void c_square(int n, double* array_in, double* array_out)
	{
		for (int i = 0; i < n; i++)
			array_out[i] = array_in[i] * array_in[i];
	}

	C_SDK_EXPORTED void c_square_wcallback(int n, double* array_in, double* array_out)
	{ //return the square of array_in of length n in array_out
		int i;
		double percent = 0.2;
		for (i = 0; i < n; i++)
		{
			if ((double)i / n > percent)
			{
				percent = tell_python(percent);
			}
			array_out[i] = array_in[i] * array_in[i];
		}
	}

	C_SDK_EXPORTED char* hello(char* name)
	{
		printf("in C - input sting: %s\n", name);
		char hello[] = "Hello ";
		char excla[] = "!";
		char* greeting = (char*)malloc(sizeof(char) * (strlen(name) + strlen(hello) + strlen(excla) + 1));
		if (greeting == NULL) exit(1);
		strcpy(greeting, hello);
		strcat(greeting, name);
		strcat(greeting, excla);
		printf("in C - allocated %p: %s\n", greeting, greeting);
		return greeting;
	}

	C_SDK_EXPORTED void passPointerArray(int size, char** stringArray)
	{
		for (int counter = 0; counter < size; counter++)
			printf("in C: string number %d is: %s\n", counter, stringArray[counter]);
	}

	C_SDK_EXPORTED double* add_vector(double* a, double* b, int len)
	{
		double* c = new double[len];
		for (int i = 0; i < len; ++i)
			c[i] = a[i] + b[i];
		return c;
	}

	C_SDK_EXPORTED void free_mem(double* a)
	{
		delete[] a;
	}

	C_SDK_EXPORTED void add_one_to_string(char* input)
	{
		printf("in C - input sting: %s\n", input);
		for (int ii = 0; ii < strlen(input); ii++)
			input[ii]++;
	}

	C_SDK_EXPORTED char* alloc_C_string(void)
	{
		char* phrase = strdup("I was written in C");
		printf("in C: allocated %p: %s\n", phrase, phrase);
		return phrase;
	}

	C_SDK_EXPORTED void free_C_string(char* ptr)
	{
		printf("in C: free %p: %s\n", ptr, ptr);
		free(ptr);
	}


	struct vector_double /* defines a vector of doubles */
	{
		int d; /* number of elements */
		double* vec; /* ptr to vector elements*/
	};

	/* Simple structure for ctypes example */
	typedef struct {
		int x;
		int y;
	} Point;

	/* Compound C structure for our ctypes example */
	typedef struct {
		Point start;
		Point end;
	} Line;

	/* Display a Point value */
	C_SDK_EXPORTED void show_point(Point point) {
		printf("in C: Point (%d, %d)\n", point.x, point.y);
	}

	/* Increment a Point which was passed by value */
	C_SDK_EXPORTED void move_point(Point point) {
		show_point(point);
		point.x++;
		point.y++;
		show_point(point);
	}

	/* Increment a Point which was passed by reference */
	C_SDK_EXPORTED void move_point_by_ref(Point* point) {
		show_point(*point);
		point->x++;
		point->y++;
		show_point(*point);
	}

	/* Return by value */
	C_SDK_EXPORTED Point get_point(void) {
		static int counter = 0;
		Point point = { counter++, counter++ };
		printf("in C: Point (%d, %d)\n", point.x, point.y);
		return point;
	}

	void show_line(Line line) 
	{
		printf("C:show_line: (%d, %d)->(%d, %d)\n",
		line.start.x, line.start.y,
		line.end.x, line.end.y);
	}

	void shift_line(Line* line) 
	{
		move_point_by_ref(&line->start);
		move_point_by_ref(&line->end);
	}

	C_SDK_EXPORTED Line get_line(void) {
		Line l = { get_point(), get_point() };
		return l;
	}

	C_SDK_EXPORTED void fill_data(int* pi, double* pd, char* ps)
	{
		if (pi) *pi = 5;
		if (pd) *pd = 10.12;
		if (ps)
		{
			strcpy(ps, "kuku");
		}
	}
}