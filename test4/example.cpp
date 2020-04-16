#include "example.h"

void Example::add(int x, int y, int* result){
    *result = x + y;
}

int Example::sub(int *x, int *y){
    return *x - *y;
}

void Example::say_hello(){
    cout << "hello world!" << endl;
}

void Example::negate(int *x){
    *x = -(*x);
}
