// Stores and prints an integer's address

#include <stdio.h>

int main(void)
{
    int n = 50;
    int *p = &n;
    int *p1=&n;
    printf("%i\n",*p1);
    printf("%p\n", p);
    printf("%p\n", &n);
}
