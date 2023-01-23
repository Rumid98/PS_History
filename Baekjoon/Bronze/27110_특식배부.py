import sys
input = sys.stdin.readline
n = int(input())
chickens = list(map(int, input().split()))
answer = 0


for i in range(3):
    if chickens[i] <= n:
        answer += chickens[i]
    else:
        answer += n
sys.stdout.write(str(answer))
