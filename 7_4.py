list1 = [0,0,0,0,0]


while True :
      choice = int(input('몇 번 후보자를 선택하시겠습니까?(종료 -1) : '))

      if choice == -1:
            break

      if choice < 1 or choice > 5:
            print('그런 후보자 없음')
            continue

      if choice == 1:
            list1[0] += 1
      elif choice == 2:
            list1[1] += 1
      elif choice == 3:
            list1[2] += 1
      elif choice == 4:
            list1[3] += 1
      elif choice == 5:
            list1[4] += 1

print('후보자번\t득표결과')
top = 0
num = 0

for i in range(5):
      if list1[i] > top:
            top = list1[i]
            num = i+1
      print('\t%d\t%d'% ((i+1), list1[i]))
      

print('====> 후보자번호 %d번이 과대로 선출되었습니다.'  % (num))
