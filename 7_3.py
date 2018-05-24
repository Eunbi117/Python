import random

list1 = []
list2 = []
total, aver = 0, 0

for i in range(10):
      for j in range(3):
            list1.append(random.randrange(1,100))
            total += list1[j]
      list1.append(total)
      list1.append(total/3.0)
      list2.append(list1)
      list1 = []
      total, aver = 0, 0


print('학번\t시험1\t시험2\t시험3\t합\t평균')
print('==========================================')

for i in range(10):
      print('%d\t' % (i+1), end='')
      for j in range(3):
            print('%d\t'%( list2[i][j]), end='')
      print('%d\t%.2f' % (list2[i][j+1], list2[i][j+2]))
      print()


maxscore, minscore = 0,100

for i in range(10):
      if list2[i][0] > maxscore:
            maxscore = list2[i][0]
      if list2[i][0] < minscore:
            minscore = list2[i][0]

print('시험1 최대점수: %d 최소점수: %d' % (maxscore, minscore))

maxscore, minscore = 0,100

for i in range(10):
      if list2[i][1] > maxscore:
            maxscore = list2[i][0]
      if list2[i][1] < minscore:
            minscore = list2[i][0]

print('시험2 최대점수: %d 최소점수: %d' % (maxscore, minscore))

maxscore, minscore = 0,100

for i in range(10):
      if list2[i][2] > maxscore:
            maxscore = list2[i][0]
      if list2[i][2] < minscore:
            minscore = list2[i][0]

print('시험3 최대점수: %d 최소점수: %d' % (maxscore, minscore))
