import base64

def base64_to_ascii(base64_string):
    """ Convert base64 encoding to ASCII text"""
    try:
        # Decode the base64 string to bytes
        bytes_object = base64.b64decode(base64_string)
        # Convert the bytes to ASCII
        ascii_string = bytes_object.decode("ASCII")
        return ascii_string
    except (ValueError, UnicodeDecodeError):
        return "Invalid Base64 input or non-ASCII characters"


print(base64_to_ascii("bG9sbGlwb3A="))
