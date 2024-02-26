
import time, socket, sys

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))

s.listen()
print("\nWaiting for incoming connections...\n")
communication_socket, addr = s.accept()
"""here conn is the endpoint(socket) that the server  will use to send/receive
 data from client .the above socket will be for listening and accepting while this is for communication with a particular client"""
# print(conn,addr)
print("Received connection from ", addr[0], "(", addr[1], ")\n")

c_name = communication_socket.recv(1024).decode() #1024 is the buffer size the amount of data we will receive
 # since we transfer data as streams  not as strings so we need to decode it
print(c_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
communication_socket.send(name.encode())

while True:
    msg=communication_socket.recv(1024).decode()
    print(c_name, ":", msg)
    msg = input(str("Me : "))
    if msg == "[e]":
        msg = "Left chat room!"
        communication_socket.send(msg.encode())
        print("\n")
        break
    communication_socket.send(msg.encode())














    # message = input(str("Me : "))
    # if message == "[e]":
    #     message = "Left chat room!"
    #     communication_socket.send(message.encode())
    #     print("\n")
    #     break
    # communication_socket.send(message.encode())
    # message = communication_socket.recv(1024).decode()
    # print(c_name, ":", message)
