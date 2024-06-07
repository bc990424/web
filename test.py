import socket , turtle , threading
import numpy as np

t = turtle.Turtle()
turtle.title("31001 강민석,31017 이송주, 파이썬을 이용한 오목")
t.hideturtle()
t.speed(0)
turtle.bgcolor("#DEB887")

a = np.zeros((16, 16))

class omok:
    def __init__(self):
        self.dx = [-1, 1, -1, 1, 0, 0, 1, -1]
        self.dy = [0, 0, -1, 1, -1, 1, -1, 1]

    def move(self, x, y, m):
        if a[x, y] == 0:
            for i, n in zip(self.dx, self.dy):
                count = 0
                for z in range(1, 6):
                    if 0 <= x + i * z < 16 and 0 <= y + n * z < 16:
                        if a[x + i * z, y + n * z] == m:
                            count += 1
                        else:
                            break
                if count == 5:
                    print("승")
                    return
            a[x, y] = m

    def q(self, a, b):
        t.pu()
        t.goto(-400, 400)
        t.seth(a)
        t.pd()
        for n in range(16):
            t.fd(50)
            t.rt(b)
            t.fd(800)
            t.bk(800)
            t.lt(b)

    def init(self):
        self.q(0, 90)
        self.q(270, 270)

    def locate(self,x,y,n):
        t.pu()
        t.goto(-420+50*x ,400-50*y)
        t.pd()
        t.begin_fill()
        t.color("white" if n == 1 else "black")
        t.circle(20)
        t.end_fill()

    def place_stone(self,x, y):
        # Convert mouse click position to grid coordinates
        grid_x = int((x + 420) // 50)
        grid_y = int((420 - y) // 50)
        # Place stone at the corresponding grid position
        self.locate(grid_x, grid_y, 1)

w = omok()

# TCP/IP 소켓 생성
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 서버의 주소와 포트를 정의합니다.
server_address = ('10.24.32.115', 12345)

# 소켓을 서버에 연결합니다.
client_socket.connect(server_address)
def so():
    try:
        while True:
        # 사용자로부터 메시지를 입력받습니다.
            nickname = input("닉내임을 입력하세요")

        # 서버로 메시지를 전송합니다.sd
            client_socket.sendall(nickname.encode())

        # 서버로부터 응답을 받습니다.
            my_color = client_socket.recv(1024).decode()
            game = True
            turtle.onscreenclick(w.place_stone)




    finally:
    # 소켓을 닫습니다.
        client_socket.close()
