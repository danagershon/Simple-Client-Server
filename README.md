Network Security HW2: implementing simple client server programs in python

** files:

client.py:
implementation of client program using python socket module. 
use: python client.py hostname port
the program connects to specified host on the specified port and sends a HTTP GET request

server.py
implementation of server program using python socket module. 
use: python server.py port
the program listens on the specified port for client connections and sends "example.html"

example.html:
simple web page for the server to send to clients
