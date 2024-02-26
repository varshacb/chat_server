import time, socket, sys

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

c = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)
# this is only for mentioning the hostnam eand ip address of the client we will not use it to bind the socket

print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
name = input(str("\nEnter your name: "))
port = 1234
print("\nTrying to connect to ", host, "(", port, ")\n")
time.sleep(1)
c.connect((host, port))
print("Connected...\n")

c.send(name.encode())
server_name = c.recv(1024)
server_name = server_name.decode()
print(server_name, "has joined the chat room\nEnter [e] to exit chat room\n")

while True:
    msg=input(str("Client(Me):"))
    if msg == "[e]":
        msg = "Leaving chat room!"
        c.send(msg.encode())
        print("\n")
        break
    c.send(msg.encode())
    msg = c.recv(1024).decode()
    print(server_name,":",msg)