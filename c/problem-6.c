#include <stdio.h>

int main(int argc, char *argv[])
{
    int sum = 0, sum_squared = 0, square_sum = 0, diff = 0;

    for(int i = 1; i <= 100; i++) {
        sum += i;
        square_sum += i * i;
    }

    diff = square_sum - (sum * sum);
    printf("%d\n", diff);
    return 0;
}
