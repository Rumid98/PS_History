from sys import stdin, stdout
input = stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]


sums = [[0]*(n+1) for _ in range(n+1)]  # 구간합 저장 배열
for i in range(1, n+1):
    for j in range(1, n+1):
        sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + graph[i-1][j-1]
for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    stdout.write(str(sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1]) + '\n')
