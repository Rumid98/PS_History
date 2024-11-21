import sys
input = sys.stdin.readline


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
shinei_mod = 0
answer = True

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            shinei_mod = (i+j) % 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and (i+j)%2 == shinei_mod:
            answer = False
print('Lena') if answer else print('Kiriya')
