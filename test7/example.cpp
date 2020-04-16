#include "example.h"

void getname(vector<string> vecstr){
    vector<string>::iterator it = vecstr.begin();
    for (; it != vecstr.end(); ++it)
        cout << *it << endl;

}

void getnumber(vector<int> vecint){
    vector<int>::iterator it = vecint.begin();
    for (; it != vecint.end(); ++it)
        cout << *it << endl;

}
