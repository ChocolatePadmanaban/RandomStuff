#include <stdio.h>
#include <string.h>

void to_upper(char* string)
{
    const char OFFSET = 'a' - 'A';
    while (*string)
    {
        *string = (*string >= 'a' && *string <= 'z') ? *string -= OFFSET : *string;
        string++;
    }
}

int main() {
    int no_of_tests;
    scanf("%d",&no_of_tests);
    for(int i=0;i<no_of_tests;i++){
        char a_string[100000] , b_string[100000];
        scanf("%s",a_string);
        scanf("%s",b_string);
        to_upper(a_string);
        to_upper(b_string);
        int common_len=strlen(a_string);
        int common_count=0;
        for(int j=0; j<common_len;j++){
            for(int k=0;k<strlen(b_string);k++){
                if(a_string[j]==b_string[k]){
                    b_string[k]='0';
                    break;
                }
            }
        }
        for(int j=0; j<strlen(b_string);j++){
            if(b_string[j]=='0'){
                common_count++;
            }
        }
        printf("%d\n",strlen(a_string)+strlen(b_string)-2*common_count);

    }
    return 0;
}