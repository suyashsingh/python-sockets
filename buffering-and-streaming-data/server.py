import socket
HEADER_SIZE = 10 # bytes
MSG = "Welcome to the server!"

def addHeader(data):
    return (f"{len(data):<{HEADER_SIZE}}" + data).encode("utf-8")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientsocket.send(addHeader(MSG))
    # Closing the client connection is not needed, as cliet knows how much data
    # is comming from the header
    #clientsocket.close()