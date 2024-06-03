import socket

# TCP/IP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버의 주소와 포트를 정의합니다.
server_address = ('localhost', 12345)

# 소켓을 서버에 연결합니다.
client_socket.connect(server_address)

try:
    while True:
        # 사용자로부터 메시지를 입력받습니다.
        message = input("보낼 메시지를 입력하세요 (종료하려면 'exit' 입력): ")
        if message == 'exit':
            break

        # 서버로 메시지를 전송합니다.sd
        client_socket.sendall(message.encode())

        # 서버로부터 응답을 받습니다.
        response = client_socket.recv(1024)
        print("서버로부터 받은 응답:", response.decode())

finally:
    # 소켓을 닫습니다.
    client_socket.close()
