import sys
input = sys.stdin.readline
n = int(input())


graph = [[' '] * n for _ in range(n)]
graph[0][0] = '*'
count = 0
tmp = n
while tmp != 1:
    tmp = tmp // 3
    count += 1
for i in range(count):
    start_bound = [row[0:3**i] for row in graph[0:3**i]]
    di = [[3**i, 0], [2*3**i, 0], [2*3**i, 3**i], [2*3**i, 2*3**i], [3**i, 2*3**i], [0, 2*3**i], [0, 3**i]]
    for j in range(7):
        for k in range(3**i):
            for l in range(3**i):
                graph[di[j][0]+k][di[j][1]+l] = start_bound[k][l]
for i in range(n):
    for j in range(n):
        sys.stdout.write(graph[i][j])
    sys.stdout.write('\n')
