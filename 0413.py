for i in range(2, 51):
      for j in range(2, i+1):
            if i % j == 0:
                  if i == j:
                        print(i, end=" ")
                  break
