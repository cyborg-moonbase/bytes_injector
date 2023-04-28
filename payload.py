"""
Creates an injectable payload from an executable binary.
"""

import builtins
from sys import argv
from base64 import b64encode

# input should be a windows executable
input_binary = argv[1]
# output can be a .txt or file with any suffix
output_payload = argv[2]

def make_payload(input_bin, output_file):
    with open(input_bin, mode='rb') as f:
        x = f.read()
        byte_array = bytearray(x)
        payload = f"global payload; payload = {byte_array}"
        encoded_payload = b64encode(payload.encode('utf-8'))
        with open(output_file, mode='w', encoding='utf-8') as g:
            g.write(encoded_payload.decode('utf-8'))
            
            
if __name__ == '__main__':
    make_payload(input_binary, output_payload)
