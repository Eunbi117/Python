hexnum = input('16진수 한글자 입력 : ')

if('0' <= hexnum <='9'):
      print('10진수 ==> ', int(hexnum))

elif(hexnum >= 'A' and hexnum <= 'F'):
      print('10진수 ==> ', int(hexnum, 16))

else:
      print('16진수가 아닙니다.')
