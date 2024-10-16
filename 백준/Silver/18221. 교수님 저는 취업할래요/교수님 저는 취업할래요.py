import sys
input = sys.stdin.readline


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
position = [[0, 0], [0, 0]]
distance = 0
count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            position[0][0], position[0][1] = i, j
        if graph[i][j] == 5:
            position[1][0], position[1][1] = i, j

if ((position[0][0]-position[1][0])**2 + (position[0][1]-position[1][1])**2)**0.5 < 5:
    print(0)
else:
    for i in range(min(position[0][0], position[1][0]), max(position[0][0], position[1][0])+1):
        for j in range(min(position[0][1], position[1][1]), max(position[0][1], position[1][1])+1):
            if graph[i][j] == 1:
                count += 1
    if count >= 3:
        print(1)
    else:
        print(0)
