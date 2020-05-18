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

2. **improved-client-server**
    + The server program is same as that of **simple-client-server** changes are
    in the client.
    + The client earlier requested *1024 bytes* of data from the server now
    instead it requests only *8 bytes* of data on one go. It keeps listening and
    stiches together the data and displays it on the console.
    + The essential condition is for the server to break connection with the 
    client so that the client knows it should not wait for more data.
    + When server breaks connection client recievs *0 bytes* of data as an 
    indication of no more data.
    + Running the program is same as **simple-client-server**
