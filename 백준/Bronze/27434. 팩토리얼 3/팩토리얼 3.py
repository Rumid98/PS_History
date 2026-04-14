import sys
input = sys.stdin.readline

n = int(input())
answer = 1
if n <= 1:
    print(1)
else:
    for i in range(2, n+1):
        answer *= i
    print(answer)