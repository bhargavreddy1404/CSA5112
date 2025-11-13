#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define SIZE 5

void generateKeyMatrix(char key[], char keyMatrix[SIZE][SIZE]) {
    int i, j, k;
    int dict[26] = {0};
    char tempKey[26];
    int idx = 0;

        for (i = 0; key[i]; i++) {
        char ch = toupper(key[i]);
        if (ch == 'J') ch = 'I';
        if (isalpha(ch) && dict[ch - 'A'] == 0) {
            tempKey[idx++] = ch;
            dict[ch - 'A'] = 1;
        }
    }

       for (i = 0; i < 26; i++) {
        if (i + 'A' == 'J') continue;
        if (dict[i] == 0) tempKey[idx++] = i + 'A';
    }

    // Fill 5x5 matrix
    k = 0;
    for (i = 0; i < SIZE; i++)
        for (j = 0; j < SIZE; j++)
            keyMatrix[i][j] = tempKey[k++];
}


void findPosition(char keyMatrix[SIZE][SIZE], char ch, int *row, int *col) {
    int i, j;
    if (ch == 'J') ch = 'I';
    for (i = 0; i < SIZE; i++)
        for (j = 0; j < SIZE; j++)
            if (keyMatrix[i][j] == ch) {
                *row = i;
                *col = j;
                return;
            }
}

void encryptPair(char a, char b, char keyMatrix[SIZE][SIZE], char *out) {
    int r1, c1, r2, c2;
    findPosition(keyMatrix, a, &r1, &c1);
    findPosition(keyMatrix, b, &r2, &c2);

    if (r1 == r2) {
        // Same row
        out[0] = keyMatrix[r1][(c1 + 1) % SIZE];
        out[1] = keyMatrix[r2][(c2 + 1) % SIZE];
    } else if (c1 == c2) {
        // Same column
        out[0] = keyMatrix[(r1 + 1) % SIZE][c1];
        out[1] = keyMatrix[(r2 + 1) % SIZE][c2];
    } else {
        // Rectangle rule
        out[0] = keyMatrix[r1][c2];
        out[1] = keyMatrix[r2][c1];
    }
}

int main() {
    char key[30], plaintext[100], prepared[100], ciphertext[100];
    char keyMatrix[SIZE][SIZE];
    int i, j, k = 0;

    printf("Enter the keyword: ");
    scanf("%s", key);
    getchar(); // clear newline

    printf("Enter the plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);
    plaintext[strcspn(plaintext, "\n")] = 0; // remove newline

       generateKeyMatrix(key, keyMatrix);

    printf("\nKey Matrix (5x5):\n");
    for (i = 0; i < SIZE; i++) {
        for (j = 0; j < SIZE; j++)
            printf("%c ", keyMatrix[i][j]);
        printf("\n");
    }

    
    k = 0;
    for (i = 0; plaintext[i]; i++) {
        char ch = toupper(plaintext[i]);
        if (isalpha(ch)) {
            if (ch == 'J') ch = 'I';
            prepared[k++] = ch;
        }
    }

        char temp[200];
    j = 0;
    for (i = 0; i < k; i += 2) {
        temp[j++] = prepared[i];
        if (i + 1 < k) {
            if (prepared[i] == prepared[i + 1])
                temp[j++] = 'X';
            temp[j++] = prepared[i + 1];
        } else {
            temp[j++] = 'X'; // padding
        }
    }
    temp[j] = '\0';

    // Encrypt in pairs
    for (i = 0; i < j; i += 2)
        encryptPair(temp[i], temp[i + 1], keyMatrix, &ciphertext[i]);

    ciphertext[j] = '\0';

    printf("\nEncrypted text: %s\n", ciphertext);

    return 0;
}
