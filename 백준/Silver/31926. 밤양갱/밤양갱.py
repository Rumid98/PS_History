import sys
input = sys.stdin.readline

n = int(input())
answer = 8
for i in range(100):
    if 2**i == n:
        answer += (i+2)
        break
    elif 2**i > n:
        answer += (i+1)
        break
print(answer)
