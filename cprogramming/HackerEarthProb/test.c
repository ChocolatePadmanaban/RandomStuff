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

void main() {
    char a[100000];
    scanf("%s", a);
    printf("%d\n",strlen(a));
    to_upper(a);
    printf("%c\n", a[2]);
    
}