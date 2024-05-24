import turtle
from PIL import Image
import numpy as np
im = Image.open('media.png')
a = np.asarray(im)
print(a)
class draw:
    def __init__(self):
        turtle.speed(0)
        turtle.hideturtle()
        turtle.pensize(2)
        turtle.pu()
        turtle.setposition(-470,400)

    def move(self,a):

        for i in a:
            f=1
            for n in i:
                if n == 1 : turtle.pd()
                turtle.fd(2)
                turtle.pu()
            turtle.setposition(-470, 400-f*2)
            f +=1
a=draw()
a.move([[0,1,0,0,0,0,1,0,1,1,0],
       [1,0,0,0,1,1,0,1,1,1,0]])
turtle.mainloop()