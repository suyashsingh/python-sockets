# Client to recieve data in chunks instead of recieving the entire message once

import socket
import sys

HEADER_SIZE = 10 # bytes
CLIENT_BUFFER_SIZE = 15 # This must be >= HEADER_SIZE
IP = '127.0.0.1'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

while True:
    msg = ''
    is_new_msg = True

    while True:
        msg_chunk = s.recv(CLIENT_BUFFER_SIZE).decode("utf-8")

        if len(msg_chunk) <= 0:
            # server closed connection
            # exit here
            sys.exit()

        # Find the msg length if the message is new
        if is_new_msg:
            msg_len = int(msg_chunk[:HEADER_SIZE])
            is_new_msg = False # Ain't new anymore!
        
        # Combine the chunks
        msg += msg_chunk

        # Have you recieved the entire message
        if len(msg) - HEADER_SIZE == msg_len:
            is_new_msg = True
            print(msg[HEADER_SIZE:])
            break