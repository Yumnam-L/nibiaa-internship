import socket

SERVER_IP = "127.0.0.1" 
SERVER_PORT = 9999

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    print("Message sent!")

if __name__ == "__main__":
    while True:
        msg = input("Enter message: ")
        send_message(msg)