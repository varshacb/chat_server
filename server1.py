import socket
import threading
import queue

# Constants
NUM_SERVERS = 3
HOST = '127.0.0.1'  # localhost
PORT_BASE = 5555

# Function to handle each client
def handle_client(client_socket, client_address):
    print(f"Connected to {client_address}")
    try:
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if not message:
                break
            print(f"Received from {client_address}: {message}")
            # Here, you can perform operations specific to this client's session
            # For example, store messages in a database, process commands, etc.
    except Exception as e:
        print(f"Error handling client message: {e}")
    finally:
        client_socket.close()
        print(f"Closed connection with {client_address}")

# Function to distribute clients among servers in a round-robin manner
def assign_server():
    while True:
        client_socket, client_address = clients.get()
        server_socket = server_sockets[server_index.get()]
        server_index.put((server_index.get() + 1) % NUM_SERVERS)  # Round-robin assignment
        server_socket.put((client_socket, client_address))

# Function to start handling clients on a server
def start_server(server_socket):
    while True:
        client_socket, client_address = server_socket.get()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# Main function to start the server
def main():
    try:
        global server_sockets
        global server_index
        global clients

        server_sockets = []
        server_index = queue.Queue()
        clients = queue.Queue()

        # Create server sockets
        for i in range(NUM_SERVERS):
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.bind((HOST, PORT_BASE + i))
            server_socket.listen()
            server_sockets.append(server_socket)

        print("Chat servers started.")

        # Start thread to distribute clients among servers
        assign_thread = threading.Thread(target=assign_server)
        assign_thread.start()

        # Start threads to handle clients on each server
        server_threads = []
        for server_socket in server_sockets:
            server_thread = threading.Thread(target=start_server, args=(queue.Queue(),))
            server_threads.append(server_thread)
            server_thread.start()

        # Wait for all server threads to finish
        for server_thread in server_threads:
            server_thread.join()

    except Exception as e:
        print(f"Error starting server: {e}")
    finally:
        for server_socket in server_sockets:
            server_socket.close()

if __name__ == "__main__":
    main()
