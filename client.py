import socket

HOST = "127.0.0.1"
PORT = 10000

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((HOST, PORT))
        print(f"connected to server in : {HOST} : {PORT}")

        welcome = client_socket.recv(1024).decode('utf-8')
        print(welcome)

        while True:
            message = input("send message to server or exit ")
            if message.lower() == "exit":
                break

            client_socket.sendall(message.encode('utf-8'))

            response = client_socket.recv(1024).decode('utf-8')
            print(f"server {response}")

    except ConnectionRefusedError:
        print("connection failed")
    finally:
        client_socket.close()


if __name__ == "__main__":
    start_client()
