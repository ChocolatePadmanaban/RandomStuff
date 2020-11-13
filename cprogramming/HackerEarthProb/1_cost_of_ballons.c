#include <stdio.h>

int Find_min(int a , int b){
    if (a>b){
        return b;
    }
    else
    {
        return a;
    }
    
}




int main() {
    int num_of_tests, cost_of_green , cost_of_purple, num_of_participants;
    scanf("%d", &num_of_tests); 
    int output_arr[num_of_tests];
    for (int i=0; i<num_of_tests;i++)
    {
        scanf("%d %d", &cost_of_green, &cost_of_purple); 
        scanf("%d", &num_of_participants);
        int output_a=0;
        int output_b=0;
        for (int j=0; j<num_of_participants; j++)
        {
            int a,b;
            scanf("%d %d", &a, &b);
            output_a=output_a+cost_of_green*a+cost_of_purple*b;
            output_b=output_b+cost_of_purple*a+cost_of_green*b;
        }

        output_arr[i]=Find_min(output_a,output_b);
    }
    for(int i=0; i<num_of_tests;i++){
        printf("%d\n",output_arr[i]);
    }
    return 0;
}


// sample input:
// 2
// 9 6
// 10
// 1 1
// 1 1
// 0 1
// 0 0
// 0 1
// 0 0
// 0 1
// 0 1
// 1 1
// 0 0
// 1 9
// 10
// 0 1
// 0 0
// 0 0
// 0 1
// 1 0
// 0 1
// 0 1
// 0 0
// 0 1
// 0 0

// sample output:
// 69
// 14