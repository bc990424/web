import numpy as np



a=np.zeros((16,16))

class omok:
    def __init__(self):
        self.dx = [-1, 1, -1, 1, 0, 0, 1, -1]
        self.dy = [0, 0, -1, 1, -1, 1, -1, 1]

    def move(self,x,y,m):
        if a[x,y] == 0:
            for i in self.dx:
                for n in self.dy:
                    try:
                        for z in range(1,6,1):
                            if not a[x+i*z,y+z*n] == m:
                                end= False
                                break
                        if end and not a[x+6*i,y+6*n] == m:
                            print("승")

                    except:
                        pass






w= omok()
w.move(2,3,4)
