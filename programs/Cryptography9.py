def prepare_key_matrix(key):
    key = key.upper().replace('J', 'I')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I/J combined
    seen = set()
    matrix = []

    # Add letters from the keyword
    for char in key:
        if char not in seen and char in alphabet:
            matrix.append(char)
            seen.add(char)

    # Add remaining letters
    for char in alphabet:
        if char not in seen:
            matrix.append(char)
            seen.add(char)

    # Convert list to 5x5 matrix
    key_matrix = [matrix[i*5:(i+1)*5] for i in range(5)]
    return key_matrix

def find_position(matrix, char):
    if char == 'J':
        char = 'I'
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None

def decrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:  # Same row
        return matrix[row1][(col1 - 1) % 5], matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 - 1) % 5][col1], matrix[(row2 - 1) % 5][col2]
    else:  # Rectangle swap
        return matrix[row1][col2], matrix[row2][col1]

def decrypt_playfair(ciphertext, key_matrix):
    ciphertext = ciphertext.replace(' ', '').upper()
    plaintext = ""
    i = 0
    while i < len(ciphertext):
        a = ciphertext[i]
        b = ciphertext[i+1] if i+1 < len(ciphertext) else 'X'
        da, db = decrypt_pair(key_matrix, a, b)
        plaintext += da + db
        i += 2
    return plaintext

# Example usage
key = "PT109"
ciphertext = """KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ"""

key_matrix = prepare_key_matrix(key)

print("Key Matrix:")
for row in key_matrix:
    print(" ".join(row))

decrypted_text = decrypt_playfair(ciphertext, key_matrix)
print("\nDecrypted message:")
print(decrypted_text)
