import socket
from database import init_db, insert_message

HOST = "0.0.0.0"  
PORT = 9999

def start_server():
    init_db()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_socket.bind((HOST, PORT))

    print(f"UDP Server started on {HOST}:{PORT}")

    while True:
        data, addr = server_socket.recvfrom(1024)

        message = data.decode()

        print(f"Received from {addr}: {message}")

        insert_message(message, str(addr))

if __name__ == "__main__":
    start_server()