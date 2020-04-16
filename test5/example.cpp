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

int Example::sumitems(const int *first, int nitems){
    int sum = 0;
    for (int i = 0; i < nitems; i++) {
        sum += first[i];
    }
    return sum;

}

void Example::print_array(double x[10]){
    for (int i = 0; i < 10; i++){
        cout << x[i] << endl;
    }
}
