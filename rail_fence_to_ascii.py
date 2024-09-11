def rail_fence(cipher_text, num_rails):
    """ Decrypt a Rail Fence Cipher given cipher text and key"""
    
    # Create a matrix to represent the rail fence
    rail = [['\n' for i in range(len(cipher_text))] for j in range(num_rails)]

    # To determine the direction of the rail pattern
    dir_down = None
    row, col = 0, 0

    # Mark the positions with a placeholder character '*'
    for i in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False

        # Place a marker in the matrix
        rail[row][col] = '*'
        col += 1

        # Move to the next row depending on the direction
        row += 1 if dir_down else -1

    # Fill the matrix with the cipher text
    index = 0
    for i in range(num_rails):
        for j in range(len(cipher_text)):
            if rail[i][j] == '*' and index < len(cipher_text):
                rail[i][j] = cipher_text[index]
                index += 1

    # Read the matrix in a zigzag manner to get the original text
    result = []
    row, col = 0, 0
    for i in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == num_rails - 1:
            dir_down = False

        # Collect the characters into the result list
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        # Move to the next row depending on the direction
        row += 1 if dir_down else -1

    return ''.join(result)

# Example usage
cipher_text = "F daS-eefn  n KZ3eheadty.YI8lta oiwy-Q0. r aI2"
num_rails = int(5)
print(rail_fence(cipher_text, num_rails))
