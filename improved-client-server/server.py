import socket

# AF_INET stands for IPV4 and SOCK_STREAM means TCP sockets
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))

# Listen for clients with a queue of 5
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    # When client socket connection is closed, client recieve 0 bytes data
    clientsocket.close()