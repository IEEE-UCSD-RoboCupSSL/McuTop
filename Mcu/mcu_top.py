import threading
import socket

NUM_BOTS = 6

TCP_IP = 'localhost'
TCP_PORTS = [0, 1, 2, 3, 4, 5]
TCP_INIT_MSG = "init"
TCP_INIT_RESPONSE = "received init msg"
TCP_BUFFER_SIZE = 1024

UDP_SEND_IP = 'localhost'
UDP_SEND_PORTS = [6, 7, 8, 9, 10, 11]
UDP_RECEIVE_IP = 'localhost'
UDP_RECEIVE_PORTS = [12, 13, 14, 15, 16, 17]

def init_tcp(id):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((TCP_IP, TCP_PORTS[id]))
    tcp_socket.send(TCP_INIT_MSG)
    tcp_msg = tcp_socket.recv(TCP_BUFFER_SIZE)
    tcp_socket.close()
    if (tcp_msg == TCP_INIT_RESPONSE):
        return True
    return False

def udp_send(id):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        server_address = (UDP_RECEIVE_IP, UDP_SEND_PORTS[id])
        data = none # get FirmwareData
        message = data.SerializeToString()
        client_socket.send(message, server_address)

def udp_receive(id):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (UDP_RECEIVE_IP, UDP_RECEIVE_PORTS[id])
    server_socket.bind(server_address)

    while True:
        message, address = server_socket.recvfrom(TCP_BUFFER_SIZE)
        command = FirmwareAPI.FirmwareCommand()
        command.ParseFromString(message)
        # do something with FirmwareCommand

for id in range(0, NUM_BOTS):
    if (init_tcp(id)):
        threading.Thread(target=udp_receive, args=(id, ))
        threading.Thread(target=udp_send, args=(id, ))