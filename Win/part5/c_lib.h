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

}