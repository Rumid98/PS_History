import sys
input = sys.stdin.readline


M = int(input())
N = int(input())
i = 1
answer = []

while i*i <= N:
    if i*i >= M:
        answer.append(i*i)
    i += 1

if answer:
    print(sum(answer))
    print(answer[0])
else:
    print('-1')
    