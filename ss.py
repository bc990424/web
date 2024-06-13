import socket
import threading
import json

# 클라이언트의 닉네임과 소켓을 저장할 딕셔너리
client_dict = {}

def handle_client(client_socket, address):
    # 클라이언트의 닉네임을 받아옵니다.
    try:
        nickname = client_socket.recv(1024).decode()
        client_dict[nickname] = client_socket
        print(f"클라이언트 {nickname}({address})가 연결되었습니다.")

        # 클라이언트에게 색상을 전송합니다.
        color = "white" if len(client_dict) % 2 == 0 else "black"  # 짝수 번째 클라이언트는 흰색, 홀수 번째 클라이언트는 검정색
        client_socket.sendall(color.encode())
        while True:
            # 클라이언트로부터 돌의 위치를 받습니다.
            data = client_socket.recv(1024).decode()
            if not data:
                break  # 데이터가 없으면 연결 종료
            stone_pos = json.loads(data)
            print(f"{nickname}이(가) 돌을 놓은 위치: {stone_pos}")

            # 다른 클라이언트들에게 돌의 위치를 전송합니다.
            for client_name, client_sock in client_dict.items():
                if client_sock != client_socket:  # 자신을 제외하고
                    client_sock.sendall(data.encode())  # 다른 클라이언트에게 돌의 위치를 전송합니다.
    except Exception as e:
        print(f"클라이언트 {nickname}({address})와의 연결이 끊어졌습니다.")
    finally:
        # 클라이언트와의 연결을 종료하고 딕셔너리에서 제거합니다.
        client_socket.close()
        del client_dict[nickname]

# TCP/IP 소켓 생성
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('10.24.32.115', 1234)

# 서버의 주소와 포트를 설정하고 바인딩합니다.
server_socket.bind(server_address)

server_socket.listen(5)

print("서버가 연결 요청을 기다리고 있습니다...")

while True:
    # 클라이언트의 연결 요청을 기다립니다.
    print("연결을 기다리는 중...")
    client_socket, address = server_socket.accept()

    # 클라이언트를 처리하는 스레드를 생성하여 실행합니다.
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
