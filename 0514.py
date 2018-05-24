parking = {}
top, carName = 0, ''
select = 9

while select != 3:
      select =  int(input('<1> 자동차 넣기 <2> 자동차 빼기 <3> 끝 : '))

      if select == 1:
            if top >= 5:
                  print('주차장 꽉 참')
            else:
                  carName = input('차 이름 등록: ')
                  top += 1
                  parking[carName] = top
                  print('%s 자동차 들어감. 주차장 상태 ==>%s' % (carName, parking))               
      elif select == 2:
            if top <= 0:
                  print('나갈 자동차 없음')
            else:
                  carName = input('나갈 차 이름 검색: ')
                  if carName in parking:
                        del(parking[carName])
                        print('%s 자동차 나감. 주차장 상태 ==>%s' % (carName, parking))
                        top -= 1
                  else:
                        print('그런 차이름 없음.')
      elif select == 3:
            break;
      else:
            print('다시 입력')

print('현재 주차장에 %d대가 있음' %top)
print('프로그램 종료')
