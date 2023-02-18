
import sys
import socket

if len(sys.argv) != 2:
    print("User Alice")
    sys.exit()

# Get the PORT number from the command line argument
port = int(sys.argv[1])

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('', port)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Accept and handle incoming connections
while True:
    connection, client_address = sock.accept()
    # Handle the connection
