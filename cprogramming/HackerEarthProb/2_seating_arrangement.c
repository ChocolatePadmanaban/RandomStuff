#include <stdio.h>

int main(){
    int num_of_tests;
    scanf("%d",&num_of_tests);
    int seat_nos[num_of_tests];
    for(int i=0;i<num_of_tests;i++){
        int seat_no;
        scanf("%d",&seat_no);  
        seat_nos[i]=seat_no;
    }
    for(int i=0;i<num_of_tests;i++){
        int seat_no=seat_nos[i];
        int divident=seat_no%12;

        switch (divident)
        {
        case 1:
            printf("%d WS\n",seat_no+11 );
            break;
        case 2:
            printf("%d MS\n",seat_no+9 );
            break;
        case 3:
            printf("%d AS\n",seat_no+7 );
            break;
        case 4:
            printf("%d AS\n",seat_no+5 );
            break;
        case 5:
            printf("%d MS\n",seat_no+3 );
            break;
        case 6:
            printf("%d WS\n",seat_no+1 );
            break;
        case 7:
            printf("%d WS\n",seat_no-1 );
            break;
        case 8:
            printf("%d MS\n",seat_no-3 );
            break;
        case 9:
            printf("%d AS\n",seat_no-5 );
            break;
        case 10:
            printf("%d AS\n",seat_no-7 );
            break;
        case 11:
            printf("%d MS\n",seat_no-9 );
            break;
        case 0:
            printf("%d WS\n",seat_no-11 );
            break;
        default:
            break;
        }
    }
    return 0;
}