seat_x = 0
seats1 = []
check = 'y'

#0으로 모든 좌석 초기화
for i in range(10):
      seats1.append(0)


while True:
      if check == 'y' or check == 'Y':
            print("\n\n===========================")
            print('1  2  3  4  5  6  7  8  9  10')
            print("===========================")

            #자리 보여주기
            for i in range(0,10):
                  print(" %d" % seats1[i], end=' ')

            print()
            seat_x = int(input('==>좌석 선택 :'))
          
            if  seat_x <= 0 or seat_x > 10:
                  print('그런 좌석 없음! 다시 선택!!')
                  continue

            if seats1[seat_x - 1] == 0:
                   seats1[seat_x - 1] = 1
                   print("예약 완료!!!")
            else:
                  print('이미 예약된 좌석입니다ㅠㅠ 다시 선택!')

            check = input('계속 예약 하시겠습니까?(y or n)')
      elif check == 'n' or check == 'N':
            break
      else:
            print('다시 선택해주세요!')

                        
