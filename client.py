import socket
import sys

if __name__ == '__main__':
    # check that we got 2 arguments from command line
    if len(sys.argv) != 3:
        print("Error: expected two arguments: hostname and port")
        sys.exit(1)

    hostname = sys.argv[1]
    port = sys.argv[2]

    # check if port argument is a number
    if not port.isnumeric():
        print("Error: port specified is not a number")
        sys.exit(1)

    # check if port number is in range of legal ports
    port = int(port)
    if port < 1 or port > 65535:
        print("Error: port number is illegal")
        sys.exit(1)

    # check if hostname exists
    try:
        socket.gethostbyname(hostname)
    except socket.gaierror:
        print("Error: host name could not be resolved")
        sys.exit(1)

    # create socket for client to communicate with hostname
    client = socket.socket()
    try:
        client.connect((hostname, port))
    except socket.error:
        print("Error: could not establish connection with host")
        sys.exit(1)

    # send HTTP request to hostname and receive answer
    request = f"GET / HTTP/1.1\r\nHost: {hostname}\r\n\r\n"
    client.sendall(request.encode())
    response = client.recv(1024)
    print(response.decode())

    client.close()

