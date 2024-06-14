import socket
import threading
import json

# 클라이언트의 닉네임과 소켓을 저장할 딕셔너리
client_dict = {}

# 16x16 보드 생성
board = [[0 for _ in range(16)] for _ in range(16)]
dx = [1, 0, 1, 1]  # 방향 벡터: 가로, 세로, 대각선 2개
dy = [0, 1, 1, -1]

def check_victory(x, y, m):
    for i in range(4):
        count = 1  # 현재 돌을 포함하므로 1부터 시작
        for z in range(1, 6):
            nx, ny = x + dx[i] * z, y + dy[i] * z
            if 0 <= nx < 16 and 0 <= ny < 16 and board[nx][ny] == m:
                count += 1
            else:
                break
        for z in range(1, 6):
            nx, ny = x - dx[i] * z, y - dy[i] * z
            if 0 <= nx < 16 and 0 <= ny < 16 and board[nx][ny] == m:
                count += 1
            else:
                break
        if count >= 5:
            return True
    return False

def handle_client(client_socket, address):
    # 클라이언트의 닉네임을 받아옵니다.
    nickname = client_socket.recv(1024).decode()
    client_dict[nickname] = client_socket
    print(f"클라이언트 {nickname}({address})가 연결되었습니다.")

    # 클라이언트에게 색상을 전송합니다.
    color = "white" if len(client_dict) % 2 == 0 else "black"  # 짝수 번째 클라이언트는 흰색, 홀수 번째 클라이언트는 검정색
    client_socket.sendall(color.encode())


    try:
        while True:
            # 클라이언트로부터 돌의 위치를 받습니다.
            data = client_socket.recv(1024).decode()
            if not data:
                break  # 데이터가 없으면 연결 종료
            stone_pos = json.loads(data)
            x, y = stone_pos['x'], stone_pos['y']

            board[x][y] = 1 if color == "black" else 2

            # 돌의 위치를 다른 클라이언트에게 전송
            for client_name, client_sock in client_dict.items():
                if client_sock != client_socket:  # 자신을 제외하고
                    client_sock.sendall(data.encode())  # 다른 클라이언트에게 돌의 위치를 전송합니다.

            # 승리 조건 체크
            if check_victory(x, y, board[x][y]):
                print(f"{nickname}이(가) 승리했습니다!")
                victory_message = json.dumps({"type": "victory", "winner": nickname})
                for client_sock in client_dict.values():
                    client_sock.sendall(victory_message.encode())
                break

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
