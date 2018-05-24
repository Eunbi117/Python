a = 'python 재미있어여 1234 진짜로'
b = ''

for i in range(len(a)):
      if a[i].isdigit():
            continue
      else:
            b += a[i]

print(a, '==> ', b )
