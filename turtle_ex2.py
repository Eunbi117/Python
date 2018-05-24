import turtle as t
import random as ra

##전역 변수 선언 부분##
swidth, sheight, pSize, exitCount = 300,300,3,0
r,g,b,angle,dist,curX,curY = [0] * 7

##메인 코드 부분##
t.title('거북이가 맘대로 다니기')#제목 달기
t.shape('turtle')#거북이로 모양 잡기
t.pensize(pSize)#펜 굵기를 3으로 (변수 초기화한 부분) 설정
t.setup(width = swidth + 30, height = sheight + 30)
t.screensize(swidth, sheight)#화면 크기를 300 x 300으로 설정

while True:#무한루프
      r = ra.random()#임의의 숫자를 지정
      g = ra.random()
      b = ra.random()
      t.pencolor((r,g,b))#펜 색상을 위의 임의로 설정된 것으로 지정

      angle = ra.randrange(0,360)#0~359 사이의 임의의 숫자를 저장
      dist = ra.randrange(1,100)#1~99사이의 임의의 숫자를 저장
      t.left(angle)#거북이를 왼쪽으로 angle 의 각도만큼 움직인다
      t.forward(dist)#거북이를 앞으로 dist의 길이만큼 움직인다
      curX = t.xcor()#거북이가 있는 x좌표 저장
      curY = t.ycor()#거북이가 있는 y좌표 저장

      #x좌표나 y좌표가 범위에 있을 경우
      if(-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2):
            pass
      else:#좌표가 범위내에 없을 경우
            t.penup()#펜을 올린다
            t.goto(0,0)#거북이를 가운데로 이동한다
            t.pendown()#펜을 내린다.

            exitCount += 1#범위를 벗어날 때마다 exitCount를 1 증가시킨다

            if exitCount >= 5:#범위를 5번 이상 벗어나게 되면 
                  break#반복문을 나간

t.done()
