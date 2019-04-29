# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
args = input().split()
score_card = namedtuple('score_card', args)

tot = 0

for i in range(n):
    col_1, col_2, col_3, col_4 = input().split()
    student = score_card(col_1, col_2, col_3, col_4)
    tot += int(student.MARKS)

print("{:.2f}".format(tot/n))

#Always obey PEP-8 :))
