import sys
from collections import deque
input = sys.stdin.readline
a = list(map(int, input().split()))
b = list(map(int, input().split()))


a_score, b_score = 0, 0
result = 'D'
for i in range(10):
    if a[i] > b[i]:
        a_score += 3
        result = 'A'
    elif b[i] > a[i]:
        b_score += 3
        result = 'B'
    else:
        a_score += 1
        b_score += 1
if a_score > b_score:
    sys.stdout.write(f'{a_score} {b_score}\nA')
elif b_score > a_score:
    sys.stdout.write(f'{a_score} {b_score}\nB')
else:
    sys.stdout.write(f'{a_score} {b_score}\n' + result)
