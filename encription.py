import base64

def encode_base64(text):
    text_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('ascii')

def decode_base64(base64_string):
    base64_bytes = base64_string.encode('ascii')
    text_bytes = base64.b64decode(base64_bytes)
    return text_bytes.decode('ascii').upper()

text = input("Enter text to encode: ")
encoded_text = encode_base64(text)
print("Encoded text:", encoded_text)

decoded_text = decode_base64(encoded_text)
print("Decoded text:", decoded_text)