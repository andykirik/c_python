#pragma once

#include "export.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern "C"
{
	C_SDK_EXPORTED char* hello(char* name)
	{
		printf("in C - input sting: %s\n", name);
		char hello[] = "Hello ";
		char exclamation[] = "!";
		char* greeting = (char*)malloc(sizeof(char) * (strlen(name) + strlen(hello) + strlen(exclamation) + 1));
		if (greeting == NULL) exit(1);
		strcpy(greeting, hello);
		strcat(greeting, name);
		strcat(greeting, exclamation);
		printf("in C - allocated %p: %s\n", greeting, greeting);
		return greeting;
	}
	
	C_SDK_EXPORTED void free_C_string(char* ptr)
	{
		printf("in C: free %p: %s\n", ptr, ptr);
		free(ptr);
	}
}