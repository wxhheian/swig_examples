%module example
%include "std_vector.i"
%include "std_string.i"
%{
#define SWIG_FILE_WITH_INIT
#include "example.h"
%}


namespace std {
    %template(vectori) vector<int>;
//  %template(vectors) vector<string>;
//  %template(stringmat) vector<vector<string>>;
  %template(stringvector) vector<point>;
  %template(stringmat) vector<vector<point>>;
};

%include "example.h"
