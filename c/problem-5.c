#include <stdio.h>

int evenly_divisible(int n, int max)
{
    for(int i = 1; i <= max; i++) {
        if(n % i != 0) return 0;
    }

    return 1;
}

int main(int argc, char *argv[])
{
    int i = 20, step = 20, result;
    while(1) {
        if(evenly_divisible(i, 20)) {
            result = i;
            break;
        }

        i += step;
    }

    printf("%d\n", result);
    return 0;
}
