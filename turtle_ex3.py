import turtle as t

num = 0
swidth, sheight = 1000,300
curX, curY = 0,0

t.shape('turtle')
t.setup(width = swidth + 50, height = sheight + 50)
t.screensize(swidth, sheight)
t.penup()
t.left(90)

num = int(input('숫자입력: '))
binary = bin(num)
curX = swidth / 2
curY = 0

for i in range(len(binary)-2):
      t.goto(curX, curY)
      print(num | 0)
      if num | 0:
            t.color('red')
            t.turtlesize(2)
      else:
            t.color('blue')
            t.turtlesize(1)

      t.stamp()
      curX -= 50
      num >>= 1

t.done()
