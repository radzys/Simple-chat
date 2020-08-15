import socket
import threading
import sys


def socket_listening():
    """
    This function recieves data from server constantly
    """
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
    except ConnectionResetError:
        print('Server does not response :(')


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
""" Initializing client socket use AF_INET (IPv4 protocol) and SOCK_DGRAM (User Datagram Protocol) """
client_socket.bind(('', 0))

print("Welcome to chat, please enter server's address")
while True:
    try:  # Trying to connect with server
        address = input()
        server_address = (address, 8050)
        socket.getaddrinfo(address, 8050)
        break
    except socket.gaierror:
        print("This server does not exist, try again")

print('Enter your nickname')
nickname = input()

client_socket.sendto(f'{nickname} connected to server'.encode('utf-8'), server_address)
print(f'Welcome to server, {nickname}!')

thread = threading.Thread(target=socket_listening)
thread.start()
""" Using the threading is necessary to be able to listen to the server and the user simultaneously"""

while True:
    message = input()
    if sys.getsizeof(message) <= 1024:  # Checking size of message for avoid buffer overflow
        client_socket.sendto(f'{nickname}: {message}'.encode('utf-8'), server_address)
    else:
        print('Your message is too long, it will be not sent')
