import time as ti
from pygame import *
import threading
ga = 800
se = 800
import socket
class Main:
  def setting(self):
    init()
    self.scr = display.set_mode((ga, se))
    display.set_caption("니얼굴")
    self.clock = time.Clock()
    self.ch1_pos = [0, 0]
    self.ch1_pos = [ga / 2 - 10 / 2, se / 2 - 10]
    self.ch1_move = [0, 0]
    self.mousepos = (0, 0)
    self.bullet = False
    self.bulletli = []
    self.bulletspeed= 10
    self.emshot = True
    self.ch2_pos=[400,400]
    self.ch1_hp=10
    self.ch2_hp=10
    self.back = True
    self.game = True
    self.run()
  def run(self):
    img=threading.Thread(target=self.imgload)
    img.start()
    while self.game:
      for ev in event.get():
        if ev.type == QUIT:
          quit()
        if ev.type == KEYDOWN:
          if ev.key == K_LEFT:
            self.ch1_move[0] = -5
          if ev.key == K_RIGHT:
            self.ch1_move[0] = 5
          if ev.key == K_DOWN:
            self.ch1_move[1] = 5
          if ev.key == K_UP:
            self.ch1_move[1] = -5

        if ev.type == KEYUP:
          self.ch1_move = [0, 0]

        if ev.type == MOUSEBUTTONDOWN and ev.button == 1:
          if len(self.bulletli) <3:
            self.bulletli.append(self.shoot(self.ch1_pos,mouse.get_pos()))

      if self.ch2_hp ==0:
        self.end(True)
      elif self.ch1_hp ==0:
        self.end(False)


      self.ch1_pos[0] += self.ch1_move[0]
      self.ch1_pos[1] += self.ch1_move[1]

      # Keep character inside the screen
      if self.ch1_pos[0] < 0:
        self.ch1_pos[0] = 0
      elif self.ch1_pos[0] > ga - 20:
        self.ch1_pos[0] = ga - 20

      if self.ch1_pos[1] < 0:
        self.ch1_pos[1] = 0
      elif self.ch1_pos[1] > se - 20:
        self.ch1_pos[1] = se - 20
      self.bu(self.bulletli,True)           #총알
      display.update()
      self.back=True
      self.clock.tick(60)
  def shoot(self, c,d):
    self.bullet = True
    dx = d[0] - self.ch1_pos[0]   # x좌표 차
    dy = d[1] - self.ch1_pos[1]
    dist = (dx ** 2 + dy ** 2) ** 0.5
    result = [c, dx / dist, dy /dist]
    return result

  def emshoot(self):
    self.emshot=True
    self.ch2_hp -= 1

  def imgload(self):
    while self.game:
      if self.back:
        self.cls()
        draw.circle(self.scr, (0, 0, 0), (int(self.ch1_pos[0]), int(self.ch1_pos[1])), 20)
        draw.circle(self.scr,(200,200,200),(self.ch1_pos[0],self.ch1_pos[1]),10)
        draw.circle(self.scr,(100,100,100),(self.ch2_pos[0],self.ch2_pos[1]),20)
        draw.line(self.scr,(255,0,0),(self.ch1_pos[0]-self.ch1_hp*2,self.ch1_pos[1]+25),(self.ch1_pos[0]+self.ch1_hp*2,self.ch1_pos[1]+25),5)
        draw.line(self.scr,(255,0,0),(self.ch2_pos[0]-self.ch2_hp*2,self.ch2_pos[1]+25),(self.ch2_pos[0]+self.ch2_hp*2,self.ch2_pos[1]+25),5)
        self.back = False

  def end(self,re):
    self.game = False
    Font =font.SysFont( "arial", 140)
    a=Font.render("you {}".format("win!" if re else "lose..."),True,200)
    self.cls()
    self.scr.blit(a,[0,se/2-100])
    display.update()
    while not self.game:
      for ev in event.get():
        if ev.type == QUIT:
          quit()
          break
  def cls(self):
    self.scr.fill((255,255,255))

  def bu(self,s,ss):
    if not s == []:
      bu=0
      for i in s:
        x, y = int(i[0][0]), int(i[0][1])
        x1, y1 = x + i[1] * 3, y + i[2] * 3
        draw.line(self.scr, (255, 0, 0), (x, y), (x1, y1), 5)
        s[bu][0] = [x + self.bulletspeed * i[1], y + self.bulletspeed * i[2]]
        if x1 < 0 or x1 > ga - 20 or y < 0 or y > se - 20:
          del s[bu]
        if ss:
          if ((self.ch2_pos[0] - x1) ** 2 + (self.ch2_pos[1] - y1) ** 2) ** 0.5 < 20:
            self.emshoot()
            del self.bulletli[bu]
        bu+=1






m = Main()
m.setting()