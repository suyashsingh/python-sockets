import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

server_msg = ""
while True:
    # Request data in 8 byte chunks and put together the data
    msg = s.recv(8)
    if len(msg) <= 0:
        # The server has closed connection
        # and we dont have any more data
        break; 
    else:
        server_msg += msg.decode("utf-8")

print(msg)