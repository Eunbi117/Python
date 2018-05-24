import turtle as t
import math as m
import random as r

t1,t2,t3 = [None] * 3
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6
swidth, sheight = 300, 300

if __name__ == "__main__":
      t.title('거북이만나기')
      t.setup(width = swidth + 50, height = sheight + 50)
      t.screensize(swidth,sheight)

      t1 = t.Turtle('turtle'); t1.color('red'); t1.penup()
      t2 = t.Turtle('turtle'); t2.color('green'); t2.penup()
      t3 = t.Turtle('turtle'); t3.color('blue'); t3.penup()

      t1.goto(-100,-100); t2.goto(0,0); t3.goto(100,100)
      t1.turtlesize(2); t2.turtlesize(2); t3.turtlesize(2)

      while True:
            t1.speed(10); t2.speed(10); t3.speed(10)
            angle = r.randrange(0, 360)
            dist = r.randrange(1, 50)
            t1.left(angle); t1.forward(dist)

            angle = r.randrange(0, 360)
            dist = r.randrange(1, 50)
            t2.left(angle); t2.forward(dist)

            angle = r.randrange(0, 360)
            dist = r.randrange(1, 50)
            t3.left(angle); t3.forward(dist)

            t1X = t1.xcor(); t1Y = t1.ycor()
            t2X = t2.xcor(); t2Y = t2.ycor()
            t3X = t3.xcor(); t3Y = t3.ycor()

            #위치에서 나갔을 경우 다시 제자리로 돌아오기
            if t1X < -150 or t1X > 150 or t1Y < -150 or t1Y > 150:
                  t1.goto(-100,-100)
            if t2X < -150 or t2X > 150 or t2Y < -150 or t2Y > 150:
                  t2.goto(0,0)
            if t3X < -150 or t3X > 150 or t3Y < -150 or t3Y > 150:
                  t3.goto(100,100)

            #sqrt는 루트 계산
            #아래식은 수평 거리 구하는 공식
            if m.sqrt(((t1X - t2X) * (t1X - t2X)) + ((t1Y - t2Y) * (t1Y-t1Y))) <= 20 or \
               m.sqrt(((t1X - t3X) * (t1X - t3X)) + ((t1Y - t3Y) * (t1Y-t3Y))) <= 20 or \
               m.sqrt(((t2X - t3X) * (t2X - t3X)) + ((t2Y - t3Y) * (t2Y-t3Y))) <= 20 :
                  t1.stamp(); t2.stamp(); t3.stamp()

t.done()
               
