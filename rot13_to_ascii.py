# Decode cipher using ROT-13
def rot13(message):
    """Decode a ROT-13 Shift Cipher"""
    
    decoded = ""
    for c in message:
        if c.isalpha():
            if c.isupper():
                decoded += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
            else:
                decoded += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        else:
            decoded += c
    return decoded

print(rot13("iveghny ynxr"))
