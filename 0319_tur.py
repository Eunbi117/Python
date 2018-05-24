import turtle as t
import random as ra

def turtlestamp(x,y):
      global r,g,b
      r = ra.random()#색상 랜덤으로
      g = ra.random()
      b = ra.random()
      t.color(r,g,b)#거북이 색상 변경
      t.shapesize(ra.randrange(1,5))#터틀사이즈 랜덤으로 변경
      t.penup()
      t.goto(x,y)
      t.lt(ra.randrange(360))#거북이 각도를 왼쪽으로 얼만큼 바꿀 것인지
      t.stamp()#거북이 좌표에 찍

t.title('거북이 도장')
t.shape('turtle')

t.onscreenclick(turtlestamp, 1)

