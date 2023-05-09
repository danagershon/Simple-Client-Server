import socket
import sys

if __name__ == '__main__':
    # check that we got one argument from command line
    if len(sys.argv) != 2:
        print("Error: expected one argument: port")
        sys.exit(1)

    port = sys.argv[1]

    # check that port argument is a number
    if not port.isnumeric():
        print("Error: port specified is not a number")
        sys.exit(1)

    port = int(port)
    # check if port number is in range of legal ports
    if port < 1 or port > 65535:
        print("Error: port number is illegal")
        sys.exit(1)

    # check if port number is in not range of registered ports
    if port < 1024:
        print("Error: port number is a registered port")
        sys.exit(1)

    # create socket for server to accept client connections
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        # assign localhost address and the specified port to the socket
        try:
            server.bind(('localhost', port))
        except socket.error:
            print("Error: could not bind port")
            sys.exit(1)

        # start listening on the specified port for incoming client connection
        server.listen(1)

        # accept client connection
        client_connection, client_address = server.accept()

        with client_connection:
            client_data = client_connection.recv(1024)

            # open the supplied simple HTML page file
            web_page_file = open("example.html")
            web_page_content = web_page_file.read()
            web_page_file.close()

            # send the HTML page to the client
            response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + web_page_content
            client_connection.sendall(response.encode())
