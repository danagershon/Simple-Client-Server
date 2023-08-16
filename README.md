Network Security Course Spring 2023 HW2: implementing simple client-server programs in Python

**files:**

• client.py: client program 

The program connects to a specified host on the specified port and sends an HTTP GET request.

Uses the Python socket module.

Run: python client.py hostname port

• server.py: server program. 

The program listens on the specified port for client connections and sends "example.html".

Uses the Python socket module.

Run: python server.py port

• example.html:
simple web page for the server to send to clients
