#include <stdio.h>

int Find_min(int a , int b){
    if (a>b){
        return a;
    }
    else
    {
        return b;
    }
    
}


int min_cost_of_ballons(int  cost_of_green ,int cost_of_purple,int num_of_participants, int prize[][num_of_participants] ) {
    int sum_a =0;
    int sum_b = 0;
    for (int i=0;i<num_of_participants;i++){
        sum_a=sum_a+prize[i][0]*cost_of_green+ prize[i][1]*cost_of_purple;
        sum_b=sum_b+prize[i][0]*cost_of_purple+ prize[i][1]*cost_of_green;
    }

    return Find_min(sum_a,sum_b);
    
}



int main() {
    int num_of_tests, cost_of_green , cost_of_purple, num_of_participants;
    scanf("%d", &num_of_tests); 
    scanf("%d %d", &cost_of_green, &cost_of_purple); 
    int output_arr[num_of_tests];
    for (int i=0; i<num_of_tests;i++)
    {
        scanf("%d", num_of_participants);
        int prize[num_of_participants][2];
        for (int j=0; j<num_of_participants; j++)
        {
            int a,b;
            scanf("%d %d", &a, &b);
            prize[j][0]=a;
            prize[j][1]=b;
        }

        output_arr[i]=min_cost_of_ballons(cost_of_green , cost_of_purple, num_of_participants,prize);
        printf("%d\n",output_arr[i]);
    }
    for(int i=0; i<num_of_tests;i++){
        printf("%d\n",output_arr[i]);
    }
    return 0;
}


// int main(){
//     FILE *fptr;
//     if ((fptr = fopen("C:\\Users\\PradeepP\\Documents\\Masssssss\\RandomStuff\\cprogramming\\HackerEarthProb\\1_cost_of_ballons.c","r")) == NULL){
//         printf("Error! opening file");

//         // Program exits if the file pointer returns NULL.
//         exit(1);
//     }
//     else{
//         int num_of_tests, cost_of_green , cost_of_purple, num_of_participants;
//         printf("came else");
//         while (0<1){
//             if (scanf(fptr, "%d", &num_of_tests)==1){
//                 scanf(fptr, "%d", &num_of_tests); 
//                 scanf(fptr,"%d %d", &cost_of_green, &cost_of_purple); 
//                 printf("%d",cost_of_green);
//                 printf("hello world");
//                 for (int i=0; i<num_of_tests;i++)
//                 {   
//                     printf("hello world 1");
//                     scanf(fptr,"%d", &num_of_participants);
//                     int prize[num_of_participants][2];
//                     for (int j=0; j<num_of_participants; j++)
//                     {
//                         scanf(fptr,"%d %d", &prize[j][0],&prize[j][1]);
//                         printf("Input number is %d %d.\n", prize[j][0],prize[j][1]);
//                     }                        
//                 }
//                 fclose(fptr); 
//                 return 0;

//             } 
//         }
        
//     }
// }