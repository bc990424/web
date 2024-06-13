import socket
import turtle
import json
import threading

class OmokClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.server_address = ('10.24.32.115', 1234)

        self.client_socket.connect(self.server_address)


        self.nickname = input("닉네임을 입력하세요: ")

        self.client_socket.sendall(self.nickname.encode())
        self.my_color = self.client_socket.recv(1024).decode()
        print("나의 색상:", self.my_color)

        # 차례
        self.my_turn = True if self.my_color == "black" else False

        self.board = [[0 for _ in range(16)] for _ in range(16)]  # 로컬 보드 상태
        self.t = turtle.Turtle()
        self.turtle_setup()

    def turtle_setup(self):
        self.t.speed(0)
        turtle.title("31001 강민석,31017 이송주, 파이썬을 이용한 오목")
        self.t.hideturtle()
        turtle.bgcolor("#DEB887")
        self.q(0, 90)
        self.q(270, 270)

    def locate(self, x, y, color):
        self.t.pu()
        self.t.goto(-420 + 50 * x, 400 - 50 * y)
        self.t.pd()
        self.t.begin_fill()
        self.t.color("white" if color == "white" else "black")
        self.t.circle(20)
        self.t.end_fill()

    def q(self, a, b):
        self.t.pu()
        self.t.goto(-400, 400)
        self.t.seth(a)
        self.t.pd()
        for n in range(16):
            self.t.fd(50)
            self.t.rt(b)
            self.t.fd(800)
            self.t.bk(800)
            self.t.lt(b)

    def place_stone(self, x, y):
        if not self.my_turn:
            return

        grid_x = int((x + 420) // 50)
        grid_y = int((420 - y) // 50)

        if grid_x < 0 or grid_x >= 16 or grid_y < 0 or grid_y >= 16:
            return
        if self.board[grid_x][grid_y] == 0:
            data = {"x": grid_x, "y": grid_y}
            self.client_socket.sendall(json.dumps(data).encode())


            self.board[grid_x][grid_y] = 1 if self.my_color == "black" else 2
            self.locate(grid_x, grid_y, self.my_color)

            self.my_turn = False

    def receive_server_messages(self):
        while True:

            data = self.client_socket.recv(1024).decode()
            message = json.loads(data)

            if "type" in message and message["type"] == "victory":

                winner = message["winner"]
                self.t.clear()
                self.t.goto(0,0)
                self.t.write(f"{winner}님이 승리했습니다!",align = "center",font=("Arial", 80, "normal"))
                print(f"{winner}님이 승리했습니다!")
                turtle.exitonclick()

            else:
                # 돌의 위치 업데이트 처리
                x, y = message['x'], message['y']
                color = "black" if (self.my_color == "white") else "white"
                self.board[x][y] = 1 if color == "black" else 2
                self.locate(x, y, color)


            self.my_turn = True

    def start(self):
        threading.Thread(target=self.receive_server_messages).start()

        turtle.onscreenclick(self.place_stone)

        turtle.mainloop()

client = OmokClient()
client.start()
