import base64
import zlib

def encode (input):
    compressed = zlib.compress(input, 9)
    return base64.b64encode(compressed, '-_')

def decode (input):
    # Input is in base64url format and for some reason I have to do the replace on GAE
    base64_input = input.replace('-','+').replace('_','/')
    decoded = base64.b64decode(base64_input)
    return zlib.decompress(decoded)
