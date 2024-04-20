"""
Created on Sat Apr 20 15:28:40 2024

@author: xunya
"""

import socket

# Define the host and port
HOST = '127.0.0.1'  # Localhost
PORT = 8000        # Port to listen on

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {HOST}:{PORT}...")

while True:
    # Accept incoming connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address} established.")

    # Receive request from client
    request = client_socket.recv(1024).decode('utf-8').strip()
    print(f"Received request: {request}")

    # Send response to client
    response = request.upper()
    client_socket.sendall(response.encode('utf-8'))

    # Close the connection
    client_socket.close()