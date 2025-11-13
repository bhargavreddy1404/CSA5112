def find_position(matrix, char):
    """Find the row and column of a character in the matrix."""
    if char == 'J':
        char = 'I'
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None

def playfair_encrypt_pair(matrix, a, b):
    """Encrypt a pair of letters using Playfair rules."""
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:  # Same row
        return matrix[row1][(col1 + 1) % 5], matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 + 1) % 5][col1], matrix[(row2 + 1) % 5][col2]
    else:  # Rectangle swap
        return matrix[row1][col2], matrix[row2][col1]

def preprocess_message(message):
    """Prepare message: uppercase, replace J with I, remove non-letters."""
    message = message.upper().replace('J', 'I')
    letters = [c for c in message if c.isalpha()]
    processed = ""
    i = 0
    while i < len(letters):
        a = letters[i]
        b = letters[i+1] if i+1 < len(letters) else 'X'
        if a == b:  # Duplicate letters in pair
            processed += a + 'X'
            i += 1
        else:
            processed += a + b
            i += 2
    return processed

def playfair_encrypt(message, matrix):
    processed = preprocess_message(message)
    ciphertext = ""
    for i in range(0, len(processed), 2):
        a, b = processed[i], processed[i+1]
        ca, cb = playfair_encrypt_pair(matrix, a, b)
        ciphertext += ca + cb
    return ciphertext

# Given Playfair matrix
playfair_matrix = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

message = "Must see you over Cadogan West. Coming at once."
encrypted = playfair_encrypt(message, playfair_matrix)

print("Encrypted message:")
print(encrypted)
