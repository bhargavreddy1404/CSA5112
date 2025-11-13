#include <stdio.h>
#include <string.h>
#include <ctype.h>

void generateKey(char *plaintext, char *key, char *newKey) {
    int pLen = strlen(plaintext);
    int kLen = strlen(key);
    int i, j = 0;

    for (i = 0; i < pLen; i++) {
        if (isalpha(plaintext[i])) {
            newKey[i] = toupper(key[j % kLen]);
            j++;
        } else {
            newKey[i] = plaintext[i]; // keep spaces/punctuation aligned
        }
    }
    newKey[i] = '\0';
}

void encryptVigenere(char *plaintext, char *key, char *ciphertext) {
    int i;
    for (i = 0; plaintext[i] != '\0'; i++) {
        char p = toupper(plaintext[i]);
        char k = toupper(key[i]);

        if (isalpha(p)) {
            ciphertext[i] = ((p - 'A' + (k - 'A')) % 26) + 'A';
        } else {
            ciphertext[i] = plaintext[i]; // leave non-alphabetic unchanged
        }
    }
    ciphertext[i] = '\0';
}

int main() {
    char plaintext[100], key[100], newKey[100], ciphertext[100];

    printf("Enter the plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);
    plaintext[strcspn(plaintext, "\n")] = 0; // remove newline

    printf("Enter the key: ");
    scanf("%s", key);

    // Generate repeating key of same length as plaintext
    generateKey(plaintext, key, newKey);

    // Encrypt
    encryptVigenere(plaintext, newKey, ciphertext);

    printf("\nGenerated Key: %s", newKey);
    printf("\nEncrypted Text: %s\n", ciphertext);

    return 0;
}
