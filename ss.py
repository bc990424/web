import socket
import threading

client_list = {}
# 클라이언트 처리를 담당하는 함수


def handle_client(client_socket, address):
    while True:
        # 클라이언트로부터 데이터를 받습니다.
        data = client_socket.recv(1024)
        if not data:
            break

        client_list[data.decode()]=address[0][0:]

        # 클라이언트에게 받은 데이터를 그대로 전송합니다.
        client_socket.sendall("white".encode() if client_list != {} else "black")

        print(client_list)

    # 클라이언트와의 연결을 닫습니다.
    print(f"클라이언트 {address}와의 연결을 종료합니다.")
    client_socket.close()


# TCP/IP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.24.32.115', 12345)
cl_list = []

server_socket.bind(server_address)

server_socket.listen(5)


print("서버가 연결 요청을 기다리고 있습니다...")

while True:

    print("연결을 기다리는 중...")
    cl_list.append(server_socket.accept())
    print(f"클라이언트 {cl_list[0][0:]}가 연결되었습니다.")





    # 클라이언트를 처리하는 쓰레드를 생성하여 실행합니다.
    client_thread = threading.Thread(target=handle_client, args=(cl_list[0]))
    client_thread.start()
