seat_x, seat_y = 0,0
seats1 = []
seats2 = []
check = 'y'

#0으로 모든 좌석 초기화
for i in range(15):
      for j in range(10):
            seats1.append(0)
      seats2.append(seats1)
      seats1 = []


while True:
      if check == 'y' or check == 'Y':
            print("\n\n===========================\n")
            print("      1  2  3  4  5  6  7  8  9  10\n")
            print("===========================\n")

            #자리 보여주기
            for i in range(0,15):
                  print("%-2d | "% (i + 1), end = '')
                  for j in range(0,10):
                        print(" %d" % seats2[i][j], end=' ')
                  print('\n')

            print('==>좌석 선택(14 10) : ')
            #한줄로 받기 위함!
            inputData = input()
            splitedData = inputData.split()
            seat_x = int(splitedData[0])
            seat_y = int(splitedData[1])

            if seat_y <= 0 or seat_y > 10 or seat_x <= 0 or seat_x > 15:
                  print('그런 좌석 없음! 다시 선택!!')
                  continue

            if seats2[seat_y - 1][seat_x - 1] == 0:
                   seats2[seat_y - 1][seat_x - 1] = 1
                   print("예약 완료!!!")
            else:
                  print('이미 예약된 좌석입니다ㅠㅠ 다시 선택!')

            check = input('계속 예약 하시겠습니까?(y or n)')
      elif check == 'n' or check == 'N':
            break
      else:
            print('뭐래;;')

                        
