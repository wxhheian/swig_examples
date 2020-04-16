%module example
%include "typemaps.i"
%include "carrays.i"
%array_class(int,intArray);
%{
#define SWIG_FILE_WITH_INIT
#include "example.h"
%}

class Example
{
public:
    void add(int,int ,int* OUTPUT);
    int sub(int* INPUT , int* INPUT);
    void say_hello();
    void negate(int *INOUT);

};
