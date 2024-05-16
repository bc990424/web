import turtle
from random import *
t=turtle.Turtle()
t.speed(0)
'''
for i in range(200):
    t.pu()
    t.goto(randint(-800,800),randint(-800,800))
    t.begin_fill()
    t.color(random(),random(),random())
    si=randint(5,70)
    for x in range(5):
        t.fd(100)
        t.lt(144)
    t.end_fill()
    '''


# 태극기 짧은 줄

def short():
    t.begin_fill()
    t.fd(45)
    t.lt(90)
    t.fd(12.5)
    t.lt(90)
    t.fd(45)
    t.lt(90)
    t.fd(12.5)
    t.end_fill()

    # 태극기 긴 검은 줄(함수선언-뒤에자세히 수업)


def long():
    t.begin_fill()
    t.fd(100)
    t.lt(90)
    t.fd(12.5)
    t.lt(90)
    t.fd(100)
    t.lt(90)
    t.fd(12.5)
    t.end_fill()


# 화면 왼쪽에 있는 터틀이 가로로 이동할 때 쓰는 함수
def s1():
    t.left(180)
    t.penup()
    t.forward(18.75)
    t.pendown()
    t.right(90)


# 터틀이 세로로 이동할 떄 쓰는 함수
def s2():
    t.left(90)
    t.penup()
    t.forward(55)
    t.pendown()


# 터틀이 오른쪽으로 회전하여 세로로 이동할 때 쓰는 함수
def s3():
    t.right(90)
    t.penup()
    t.forward(55)
    t.pendown()
    t.left(180)


# 화면 오른쪽에 있는 터틀이 가로로 이동할 때 쓰는 함수
def s4():
    t.penup()
    t.forward(18.75)
    t.pendown()
    t.left(90)


# 건
t.color("black")
t.penup()
t.goto(-150, 75)
t.pendown()
t.right(45)
long()
s1()
long()
s1()
long()

# 태극기 곤
t.penup()
t.goto(100, -150)
t.pendown()
t.left(90)
short()
s2()
short()
s4()
short()
s3()
short()
s4()
short()
s2()
short()

# 태극기 감
t.penup()
t.goto(160, 75)
t.left(90)
t.forward(12.5)
t.pendown()
t.left(90)
short()
s2()
short()
s4()
t.penup()
t.back(55)
long()
s4()
short()
s2()
short()

# 태극기 리
t.penup()
t.goto(-200, -100)
t.pendown()
t.right(90)
long()
s1()
short()
s2()
short()
t.penup()
t.left(180)
t.forward(18.75)
t.left(90)
t.forward(55)
t.left(180)
t.pendown()
long()

