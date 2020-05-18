import socket
HEADER_SIZE = 10 # bytes
IP = '127.0.0.1'
PORT = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

while True:
    msg = s.recv(HEADER_SIZE)

    if len(msg) <= 0:
        # server closed the connection
        break
    else:
        # Find the data length
        temp = msg.decode("utf-8")
        data_len = int(temp[:HEADER_SIZE])
        data = s.recv(data_len).decode("utf-8")
        print(data)
