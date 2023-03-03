// Prints two strings' addresses

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get two strings
    // char *s = get_string("s: ");
    // char *t = get_string("t: ");

    char *s = "yy";
    char *t = "t: ";
    // Print strings' addresses
    printf("%p\n", &s);
    printf("%p\n", t);
    printf("%c\n", *s);
    printf("%c\n", *(s+1));
    printf("%s\n", s);
}
