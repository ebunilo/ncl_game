def hex_to_ascii(hex_string):
    """ 
    Convert  a hex string to ASCII
    It will remove any leading "0x"
    """
    ascii_string = ""
    
    # check the length of the hex string is even
    # if len(hex_string) % 2 != 0:
    #     hex_string = "0" + hex_string
    

    # strip any leading 0x
    hex_string = hex_string.replace("0x", "")

    # convert hex to ascii
    try:
        for i in range(0, len(hex_string), 2):
            hex_byte = hex_string[i:i+2]
            ascii_char = chr(int(hex_byte, 16))
            ascii_string += ascii_char
        return ascii_string
    except ValueError:
        print("Invalid hex string")

print(hex_to_ascii("0x73636f7270696f6e"))
