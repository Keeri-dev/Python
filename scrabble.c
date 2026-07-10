#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main()
{
    char player1_word[20], player2_word[20];
    int player1_score = 0, player2_score = 0;

    printf("Player 1, enter your word: ");
    scanf("%s", player1_word);
    printf("Player 2, enter your word: ");
    scanf("%s", player2_word);

    // Calculate score for Player 1
    for (int i = 0; player1_word[i] != '\0'; i++)
    {
        char letter = toupper(player1_word[i]);
        switch (letter)
        {
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
            case 'L':
            case 'N':
            case 'S':
            case 'T':
            case 'R':
                player1_score += 1;
                break;
            case 'D':
            case 'G':
                player1_score += 2;
                break;
            case 'B':
            case 'C':
            case 'M':
            case 'P':
                player1_score += 3;
                break;
            case 'F':
            case 'H':
            case 'V':
            case 'W':
            case 'Y':
                player1_score += 4;
                break;
            case 'K':
                player1_score += 5;
                break;
            case 'J':
            case 'X':
                player1_score += 8;
                break;
            case 'Q':
            case 'Z':
                player1_score += 10;
                break;
        }
    }

    // Calculate score for Player 2
    for (int i = 0; player2_word[i] != '\0'; i++)
    {
        char letter = toupper(player2_word[i]);
        switch (letter)
        {
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U':
            case 'L':
            case 'N':
            case 'S':
            case 'T':
            case 'R':
                player2_score += 1;
                break;
            case 'D':
            case 'G':
                player2_score += 2;
                break;
            case 'B':
            case 'C':
            case 'M':
            case 'P':
                player2_score += 3;
                break;
            case 'F':
            case 'H':
            case 'V':
            case 'W':
            case 'Y':
                player2_score += 4;
                break;
            case 'K':
                player2_score += 5;
                break;
            case 'J':
            case 'X':
                player2_score += 8;
                break;
            case 'Q':
            case 'Z':
                player2_score += 10;
                break;
        }
    }

    // Determine the winner
    if (player1_score > player2_score)
    {
        printf("Player 1 wins!\n");
    }
    else if (player2_score > player1_score)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }

    return 0;
}
