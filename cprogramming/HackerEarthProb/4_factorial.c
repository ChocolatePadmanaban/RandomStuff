#include <stdio.h>

int main(){
    int sing_int,fact_int=1;
    scanf("%d", &sing_int);
    for(int i = sing_int; i>0; i--){
        fact_int= fact_int*i;
    }
    printf("%d",fact_int);
}