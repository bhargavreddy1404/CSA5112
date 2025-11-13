def generate_cipher_alphabet(keyword):
    keyword = keyword.upper()  # convert keyword to uppercase
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Remove duplicates from keyword
    seen = set()
    cipher_alphabet = []
    for char in keyword:
        if char not in seen:
            cipher_alphabet.append(char)
            seen.add(char)
    
    # Add remaining letters of alphabet not in keyword
    for char in alphabet:
        if char not in seen:
            cipher_alphabet.append(char)
    
    return "".join(cipher_alphabet)

def encrypt(plaintext, cipher_alphabet):
    plaintext = plaintext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    for char in plaintext:
        if char in alphabet:
            index = alphabet.index(char)
            ciphertext += cipher_alphabet[index]
        else:
            ciphertext += char  # keep non-alphabet characters as is
    return ciphertext

def decrypt(ciphertext, cipher_alphabet):
    ciphertext = ciphertext.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""
    for char in ciphertext:
        if char in cipher_alphabet:
            index = cipher_alphabet.index(char)
            plaintext += alphabet[index]
        else:
            plaintext += char
    return plaintext

# Example usage
keyword = "CIPHER"
cipher_alphabet = generate_cipher_alphabet(keyword)
print("Cipher alphabet:", cipher_alphabet)

message = "HELLO WORLD"
encrypted = encrypt(message, cipher_alphabet)
print("Encrypted:", encrypted)

decrypted = decrypt(encrypted, cipher_alphabet)
print("Decrypted:", decrypted)
