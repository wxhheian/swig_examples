%module example
%include "typemaps.i"
%include "std_vector.i"
%include "std_string.i"

%{
#include "example.h"
#define SWIG_FILE_WITH_INIT
%}
#define STATUS 50
#define VERSION 1.1

extern double sin(double x);

extern int strcmp(const char *a, const char *b);
