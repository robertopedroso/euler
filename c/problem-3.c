#include <stdio.h>
#include <stdlib.h>

int gpf(long n)
{
    int i = 2;
    while(i * i < n) {
        while(n % i == 0) {
            n /= i;
        }

        i += 1;
    }

    return n;
}

int main(int argc, char *argv[])
{
    long n = 600851475143;
    int f = gpf(n);
    printf("%d\n", f);
    return 0;
}
