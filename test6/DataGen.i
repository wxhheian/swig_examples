//DataGen.i
%module DataGen

//用来生成指针
%include "cpointer.i"
//用来生成数组
%include "carrays.i"

%pointer_class(long, long_p);
%array_class(int, intArray);

%{
#include "DataGen.h"
%}

%include "DataGen.h"
