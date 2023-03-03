// Prints address of first char of a string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    char c = s[0];
    char *p = &c;
    string *p1=&s;
    printf("%p\n", p);
    printf("%p\n", &c);
    printf("%p\n", &s);
    printf("%p\n", p1);
    printf("%s\n", *p1);
    printf("%c\n", *p);
}
