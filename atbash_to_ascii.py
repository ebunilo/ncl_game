# Decode an atbash shift cypher
def atbash(message):
    """ Decode an atbash shift cypher"""
    cipher = ''
    for letter in message:
        if letter.isalpha():
            cipher += chr(219 - ord(letter))
        else:
            cipher += letter
    return cipher

print(atbash("hzuvob lyerlfh xzev"))
