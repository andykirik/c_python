#pragma once

#include "export.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern "C"
{
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
}