#include "example.h"




double sin(double x){
    double y;
    y = x/180*PI;
    return y;
}

int strcmp(const char *a, const char *b){
    if (a == b)
        return 0;
    else
        return -1;
}
