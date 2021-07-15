#pragma once

#include "export.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern "C"
{
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