import socket

# Constants
HOST = '127.0.0.1'  # localhost
PORT = 5555

# Main function to run the client
def main():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        print("Connected to the server.")

        # Send messages to the server
        while True:
            message = str(input("client:"))
            if message.lower() == "exit":
                print("exiting")
                client_socket.close()
                break
            client_socket.send(message.encode())
            response = client_socket.recv(1024).decode()
            print("server msg:"+response)
    except Exception as e:
        print(f"Error connecting to the server: {e}")
    # finally:
    #     # Close the socket when done
    #     client_socket.close()

if __name__ == "__main__":
    main()
