#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 1000

// Function to count frequency of each symbol
void frequencyAnalysis(char text[]) {
    int freq[256] = {0};
    int i;
    for (i = 0; text[i] != '\0'; i++) {
        if (text[i] != ' ' && text[i] != '\n')
            freq[(unsigned char)text[i]]++;
    }

    printf("\nCharacter Frequency Analysis:\n");
    printf("--------------------------------\n");
    for (i = 0; i < 256; i++) {
        if (freq[i] > 0)
            printf("%c  ->  %d\n", i, freq[i]);
    }
}

// Function to apply substitution mapping
void applyMapping(char text[], char mapFrom[], char mapTo[], int n) {
    char result[MAX];
    strcpy(result, text);

    for (int i = 0; result[i] != '\0'; i++) {
        for (int j = 0; j < n; j++) {
            if (result[i] == mapFrom[j]) {
                result[i] = mapTo[j];
                break;
            }
        }
    }

    printf("\nDecrypted Text with Current Mapping:\n");
    printf("------------------------------------\n%s\n", result);
}

int main() {
    char ciphertext[MAX] =
        "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;;]8*;:‡*8†83"
        "(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*—4)8¶8*"
        ";4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81"
        "(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;";

    printf("CIPHERTEXT:\n%s\n", ciphertext);
    frequencyAnalysis(ciphertext);

    int n;
    printf("\nEnter number of symbol mappings you want to try: ");
    scanf("%d", &n);
    getchar(); // clear newline

    char mapFrom[n], mapTo[n];
    for (int i = 0; i < n; i++) {
        printf("\nEnter ciphertext symbol #%d: ", i + 1);
        scanf("%c", &mapFrom[i]);
        getchar();
        printf("Enter plaintext letter to map it to: ");
        scanf("%c", &mapTo[i]);
        getchar();
    }

    applyMapping(ciphertext, mapFrom, mapTo, n);
    return 0;
}
