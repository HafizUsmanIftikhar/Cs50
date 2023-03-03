// Prints address of first char of a string

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s = "HI!";
    char *p = &s[0];
    string *p1=&s;
    printf("%p\n", p);
    printf("%p\n", p1);
    printf("%p\n", &s);
}
