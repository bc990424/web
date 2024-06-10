import socket, turtle, json, threading


class OmokClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 서버의 주소와 포트를 정의합니다.
        self.server_address = ('10.24.32.115', 1234)
        # 소켓을 서버에 연결합니다.
        self.client_socket.connect(self.server_address)

        # 클라이언트의 닉네임을 입력받습니다.
        self.nickname = input("닉네임을 입력하세요: ")
        # 서버에 닉네임을 전송합니다.
        self.client_socket.sendall(self.nickname.encode())
        self.my_color = self.client_socket.recv(1024).decode()
        print("나의 색상:", self.my_color)

        # 현재 차례 여부를 저장할 변수
        self.my_turn = True if self.my_color == "black" else False

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
            return  # 자신의 차례가 아니면 돌을 놓을 수 없음

        # Convert mouse click position to grid coordinates
        grid_x = int((x + 420) // 50)
        grid_y = int((420 - y) // 50)
        # Send stone position to server as JSON
        data = {"x": grid_x, "y": grid_y}
        self.client_socket.sendall(json.dumps(data).encode())

        # 현재 차례를 변경
        self.my_turn = False

    def receive_board_state(self):
        while True:
            # Receive board state from server as JSON
            data = self.client_socket.recv(1024).decode()
            board_state = json.loads(data)
            # Update board state on turtle screen
            for row in board_state:
                for cell in row:
                    self.locate(cell["x"], cell["y"], cell["color"])

            # 상대방이 돌을 놓은 후에 다시 자신의 차례가 됨
            self.my_turn = True

    def start(self):
        threading.Thread(target=self.receive_board_state).start()
        # Start listening for mouse clicks to place stones
        turtle.onscreenclick(self.place_stone)
        # Keep the turtle window open
        turtle.mainloop()


client = OmokClient()
client.start()
