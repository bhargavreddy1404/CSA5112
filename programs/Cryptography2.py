#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main() {
    char plaintext[100], ciphertext[100];
    char cipherMap[26] = {'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'};
    int i;

    printf("Enter the plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);

    for (i = 0; plaintext[i] != '\0'; i++) {
        char ch = plaintext[i];

        if (isupper(ch)) {
            ciphertext[i] = cipherMap[ch - 'A'];
        } 
        else if (islower(ch)) {
            ciphertext[i] = tolower(cipherMap[ch - 'a']);
        } 
        else {
            ciphertext[i] = ch; // keep spaces, punctuation
        }
    }
    ciphertext[i] = '\0'; // end the string

    printf("Encrypted text: %s", ciphertext);

    return 0;
}
