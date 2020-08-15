import socket

server_address = ('localhost', 8050)  # Server is running on local machine
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
""" Initializing client socket use AF_INET (IPv4 protocol) and SOCK_DGRAM (User Datagram Protocol) """
server_socket.bind(server_address)

users = []


while True:
    try:
        user_data, user = server_socket.recvfrom(1024)  # Get data from
        print(user, user_data.decode('utf-8'))
        if not user_data:
            break
        if user not in users:
            users.append(user)
        for client in users:
            if client == user:
                pass
            else:
                server_socket.sendto(user_data, client)  # Sending message from user to all users except him
    except OSError as ex:
        server_socket.close()
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(server_address)
        """Reinitializing socket in case of timeout"""
