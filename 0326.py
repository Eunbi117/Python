#변수 선언 부분
money, c50000, c10000, c5000, c1000 = 0,0,0,0,0#변수 초기화 0으로 미리 선언

#main부분
money = int(input('돈 입금: '))#input은 문자열형태이기 때문에 정수형으로 형변환 시켜준다

c50000 = money // 50000#사용자에게 받은 금액을 50000으로 나눈 몫을 저장한다
money %= 50000#50000으로 나눈 나머지를 다시 money에 저장한다

c10000 = money // 10000
money %= 10000

c5000 = money // 5000
money %= 5000

c1000 = money // 1000
money %= 1000

print('50000원 짜리 %d개' % c50000)
print('10000원 짜리 %d개' % c10000)
print('5000원 짜리 %d개' % c5000)
print('1000원 짜리 %d개' % c1000)
print('남은돈 %d' % money)