import socket
import threading

HOST = "127.0.0.1"
PORT = 10000


def handle_client(conn, addr):
    print(f"client connected in : {addr}")
    try:
        wellcom = "wellcom"
        conn.sendall(wellcom.encode('utf-8'))

        while True:
            data = conn.recv(1024)
            if not data:
                break

            data_d = data.decode("utf-8")
            print(f"got from client message : {addr} : {data_d}")

            response = f"server recive {data_d.upper()}"
            conn.sendall(response.encode('utf-8'))

    except ConnectionResetError:
        print(f"client dissconnected {addr}")
    finally:
        conn.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


if __name__ == "__main__":
    start_server()
