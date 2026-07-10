#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    char *key_str = argv[1];
    int key;

    // Check if key is a number
    if (sscanf(key_str, "%d", &key) != 1)
    {
        printf("Error: Invalid key. Key must be a positive integer.\n");
        return 1;
    }

    if (key <= 0)
    {
        printf("Error: Key must be a positive integer.\n");
        return 1;
    }

    printf("plaintext: ");
    char plaintext[100];
    fgets(plaintext, sizeof(plaintext), stdin);

    // Remove trailing newline
    plaintext[strcspn(plaintext, "\n")] = '\0';

    for (int i = 0; plaintext[i] != '\0'; i++)
    {
        if (isalpha(plaintext[i]))
        {
            char base = isupper(plaintext[i]) ? 'A' : 'a';
            plaintext[i] = (((plaintext[i] - base + key) % 26) + base);
        }
    }

    printf("ciphertext: %s\n", plaintext);
    return 0;
}
