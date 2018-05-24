a = input('문자열 넣기: ')
count = [0,0,0,0,0]#숫자, 소문자, 대문자, 한글, 특수문자 개

for i in range(len(a)):
      if a[i].isdigit():
            count[0] += 1
      elif a[i].isalpha():
            if a[i].islower():
                  count[1] += 1
            elif a[i].isupper():
                  count[2] += 1
            else:
                  count[3] += 1
      elif a[i] == ' ':
            continue
      else:
            count[4] += 1
            

print('숫자 %d개, 소문자 %d개, 대문자 %d개, 한글 %d개, 특수문자 %d개 입니다.' % (count[0], count[1], count[2], count[3], count[4]))
            
      
