%module example
%include "typemaps.i"
%include "carrays.i"
%include "cpointer.i"
%array_class(int,arrayint);
%array_class(double,doubleArray);
//%array_functions(double,doubleArray);
//%pointer_functions(int,intp);
%pointer_class(int,intp);

%{
#define SWIG_FILE_WITH_INIT
#include "example.h"
%}

class Example
{
public:
    void add(int,int,int*);
    int sub(int* INPUT, int* INPUT);
    void say_hello();
    void negate(int *INOUT);
    int sumitems(int* INPUT,int);
    void print_array(double*);
};
