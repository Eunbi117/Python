import random as r #랜덤 사용하려면 가져와야 함

com = r.randrange(3)#randrange는 괄호 안에 범위 즉 0~2까지의 수 중 임의로 하나를 저장
#만약 1~3으로 하고 싶으면 (1,4)로 하면 됨

if com == 0:
      print('가위')
elif com == 1:
      print('바위')
else:
      print('보')

