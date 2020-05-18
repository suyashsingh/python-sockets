# python-sockets
Python Socket Programming

> Note: run all the programs in *Python3*. Some of them might run on *Python2* as
    well but don't get swayed away.
1. **simple-client-server**
    + Hello world client server application.
    + `client.py` requests for 1024 bytes from the server and displays it on 
    console and exit.
    + The server has a queue of 5 clients.
    + When it gets client connection it prints the client details on the console,
    sends message and closes the client socket connection and keeps listening
    for other clients.
    + Open two terminals and run: `python3 client.py` and `python3 server.py`
