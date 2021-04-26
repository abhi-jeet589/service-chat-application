#!/usr/bin/python3
"""
Importing all the required packages
"""
import socket
import threading

'''Variable declaration '''
buffer_size = 1024
server_ip = "0.0.0.0"
server_port = 1234

'''Socket Creation'''
socket_def = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_def.bind((server_ip,server_port))

def handle_clients():
    """
    Handle the incoming clients
    """
    reference_data , clientInfo = socket_def.recvfrom(buffer_size)
    if reference_data.decode() == "Data incoming": #accepts the client when the client sends the first data as Data incoming
        socket_recv_thread = threading.Thread(target = recv)
        socket_recv_thread.start()
    else:
        pass
    return clientInfo

def recv():
    """
    Used to receive data from the client
    passed to the thread to handle multiple clients
    """
    data,clientAddr = socket_def.recvfrom(buffer_size)
    print(clientAddr[0] + ':' + str(clientAddr[1])  + '>' + data.decode())
    input()

def send(data,client):
    """
    Used to send data to the client
    """
    data = data.encode()
    socket_def.sendto(data,client)

def replyThread(data,client):
    socket_send_thread = threading.Thread(target = send , args = ((data,client)))
    socket_send_thread.start()

def reply(client):
    reply_choice = input("Do you wish to reply to this message? (Y/N)")
    if reply_choice == "Y":
        send_data = input("Enter your reply: ")
        replyThread(send_data,client)
    else:
        pass
    return True

while True :
    """
    Using an infinite loop to accept the data
    """
    try:
        client = handle_clients()
        reply(client)

    except KeyboardInterrupt:
        socket_def.close()
        exit()

