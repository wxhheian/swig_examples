%module example
%include "typemaps.i"
%{
#define SWIG_FILE_WITH_INIT
#include "example.h"
%}

void add(int,int ,int* OUTPUT);
int sub(int* INPUT, int* INPUT);
