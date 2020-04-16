/* 生成长度为10的int型数组*/
#include "DataGen.h"

long SeEd = 1234;
int FrameLen = 1024;
int main()
{
    int *SourceBbit = new int[FrameLen];
    SourceBbit = randombit_gene(SourceBbit,FrameLen,&SeEd);
    //cout << SourceBbit[0] << " " <<SourceBbit[1] << " " << SourceBbit[2] << endl;
    delete [] SourceBbit;

    return 0;
}


int* randombit_gene(int* SourceBbit,int FrameLen,long* SeEd){
    srand(*SeEd);
    for (int i = 0; i < FrameLen; i++){
        SourceBbit[i] = rand();
    }
    return SourceBbit;

}
