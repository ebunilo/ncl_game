# Convert binary to ascii
def binary_to_ascii(binary):
    """Convert a binary string to an ASCII string."""

    binary = binary.replace(" ", "") # remove any spaces from binary string
    binary_parts = [binary[i:i+8] for i in range(0, len(binary), 8)]
    ascii_string = ''
    for part in binary_parts:
        ascii_string += chr(int(part, 2))
    return ascii_string

print(binary_to_ascii("01100010 01000111 00111001 01110011 01100010 01000111 01101100 01110111 01100010 00110011 01000001 00111101"))
