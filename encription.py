import base64 # Importing the base64 library

# This encodes the text into a base64 string
def encode_base64(text):
    text_bytes = text.encode('ascii') # Converts the text into bytes
    base64_bytes = base64.b64encode(text_bytes) # Encodes the bytes into base64
    return base64_bytes.decode('ascii') # Decodes the bytes into a string and returns it

# This decodes the base64 string into a text
def decode_base64(base64_string):
    base64_bytes = base64_string.encode('ascii') # Converts the base64 string into bytes
    text_bytes = base64.b64decode(base64_bytes) # Decodes the bytes into text
    return text_bytes.decode('ascii').upper() # Decodes the bytes into a string and returns it

    # I don't know why, I did this as a seprate python file. 