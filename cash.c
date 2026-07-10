#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int cents;

    do
    {
        printf("Change owed: ");
        if (scanf("%d", &cents) != 1 || cents <= 0)
        {
            printf("Please enter a positive integer.\n");
            // Clear invalid input from buffer
            while (getchar() != '\n')
                ;
        }
    }
    while (cents <= 0);

    int coin_count = 0;

    // Greedy algorithm to minimize coins
    while (cents > 0)
    {
        if (cents >= 25)
        {
            cents -= 25;
            coin_count++;
        }
        else if (cents >= 10)
        {
            cents -= 10;
            coin_count++;
        }
        else if (cents >= 5)
        {
            cents -= 5;
            coin_count++;
        }
        else
        {
            cents -= 1;
            coin_count++;
        }
    }

    printf("%d\n", coin_count);

    return 0;
}
