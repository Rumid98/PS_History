import sys
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[0]*100 for _ in range(100)]
answer = 0

for _ in range(N):
    a1, b1, a2, b2 = map(int, input().split())
    for i in range(a1-1, a2):
        for j in range(b1-1, b2):
            graph[i][j] += 1

for i in range(100):
    for j in range(100):
        if graph[i][j] > M:
            answer += 1      

print(answer)