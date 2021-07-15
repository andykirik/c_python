#pragma once

#include "export.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern "C"
{
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
		printf("in C: show_line: (%d, %d)->(%d, %d)\n",
		line.start.x, line.start.y,
		line.end.x, line.end.y);
	}

	void move_line(Line* line) 
	{
		move_point_by_ref(&line->start);
		move_point_by_ref(&line->end);
	}

	C_SDK_EXPORTED Line get_line(void) {
		Line l = { get_point(), get_point() };
		return l;
	}
}