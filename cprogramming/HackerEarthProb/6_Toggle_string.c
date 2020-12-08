#include <stdio.h>
#include <string.h>

int main() {
    char input_sting[100];
    scanf("%s", input_sting);
    int c = 0 ;
    while(input_sting[c] != '\0'){
        printf("%c", input_sting[c]);
        c++;
    }
    return 0;
}