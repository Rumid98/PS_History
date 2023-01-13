import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]


# i번째 동전은 i-1번째 동전의 배수라는 조건 -> 가장 큰 동전부터 탐색 가능
answer = 0
for i in range(n-1, -1, -1):
    if k >= coins[i]:
        answer += (k // coins[i])
        k %= coins[i]
sys.stdout.write(str(answer))
