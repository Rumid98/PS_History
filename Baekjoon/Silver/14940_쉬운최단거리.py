from collections import deque
n, m = map(int, input().split())  # 행열 길이
graph = [list(map(int, input().split())) for _ in range(n)]  # 지도 배열
res = [[0 for _ in range(m)] for _ in range(n)]  # 결과 배열
visited = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]


# 2(목표지점) 찾기
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x, y = i, j
queue = deque()
queue.append((x, y))
while queue:
    cur = queue.popleft()
    for i in range(4):
        nx, ny = cur[0] + dx[i], cur[1] + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))
            res[nx][ny] = res[cur[0]][cur[1]] + 1
# -1 처리
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and res[i][j] == 0:
            res[i][j] = -1
# 출력
for i in range(n):
    for j in range(m):
        print(res[i][j], end=' ')
    print()
