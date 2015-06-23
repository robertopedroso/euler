#include <stdio.h>

int ispalindrome(int n)
{
    int rev = 0;
    int orig = n;

    if(n < 10) return 1;
    if(n % 10 == 0) return 0;

    while(n >= 1) {
        rev = (rev * 10) + (n % 10);
        n /= 10;
    }

    return orig == rev;
}

int main(int argc, char *argv[])
{
    int i, j, tmp, max = 0;

    for(i = 100; i < 1000; i++) {
        for(j = 100; j < 1000; j++) {
            tmp = i * j;
            if(tmp > max && ispalindrome(tmp))
                max = tmp;
        }
    }

    printf("%d\n", max);
}
