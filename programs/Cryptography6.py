#include <stdio.h>
#include <ctype.h>

// Function to find modular inverse of 'a' under mod 26
int modInverse(int a) {
    int i;
    for (i = 1; i < 26; i++) {
        if ((a * i) % 26 == 1)
            return i;
    }
    return -1;  // No inverse exists
}

// Function to encrypt text using affine cipher
void affineEncrypt(char text[], int a, int b) {
    int i;
    for (i = 0; text[i] != '\0'; i++) {
        char ch = text[i];
        if (isalpha(ch)) {
            ch = toupper(ch);
            ch = ((a * (ch - 'A') + b) % 26) + 'A';
        }
        text[i] = ch;
    }
}

// Function to decrypt text using affine cipher
void affineDecrypt(char text[], int a, int b) {
    int i, a_inv = modInverse(a);
    if (a_inv == -1) {
        printf("Decryption not possible! 'a' has no inverse mod 26.\n");
        return;
    }

    for (i = 0; text[i] != '\0'; i++) {
        char ch = text[i];
        if (isalpha(ch)) {
            ch = toupper(ch);
            ch = (a_inv * ((ch - 'A' - b + 26)) % 26) + 'A';
        }
        text[i] = ch;
    }
}

int main() {
    char text[100];
    int a, b;

    printf("Enter the text: ");
    fgets(text, sizeof(text), stdin);

    printf("Enter key a (must be coprime with 26): ");
    scanf("%d", &a);
    printf("Enter key b (0-25): ");
    scanf("%d", &b);

    affineEncrypt(text, a, b);
    printf("\nEncrypted text: %s", text);

    affineDecrypt(text, a, b);
    printf("\nDecrypted text: %s\n", text);

    return 0;
}
