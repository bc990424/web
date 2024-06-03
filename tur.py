import turtle

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

w = omok()


w.init()



w.locate(3,3,-1)

turtle.mainloop()
