Network Security Course Spring 2023 HW2: implementing simple client-server programs in Python

**files:**

• client.py:
implementation of client program using Python socket module. 

use: python client.py hostname port
the program connects to a specified host on the specified port and sends an HTTP GET request

• server.py
implementation of server program using python socket module. 

use: python server.py port
the program listens on the specified port for client connections and sends "example.html"

• example.html:
simple web page for the server to send to clients
