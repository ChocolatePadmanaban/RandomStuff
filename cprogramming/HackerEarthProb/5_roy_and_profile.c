#include <stdio.h>

int main(){
    int length, with, height,no_of_tests;
    scanf("%d", &length);
    scanf("%d",&no_of_tests);
    for(int i=0;i<no_of_tests;i++){
        scanf("%d %d", &with , &height);
        if((with < length )||( height< length)){
            printf("UPLOAD ANOTHER\n");      
        }else
        {
            if(with==height){
                printf("ACCEPTED\n");
            }else
            {
                printf("CROP IT\n");
            }
            
        }
        
    } 
    return 0;
}