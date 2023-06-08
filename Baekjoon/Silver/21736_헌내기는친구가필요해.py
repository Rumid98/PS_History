from collections import deque
n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]


def bfs(x, y):
    count = 0
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    while queue:
        cur = queue.popleft()
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:  # 범위 안에 있고 방문하지 않은 곳
                if graph[nx][ny] == 'P':
                    count += 1
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                elif graph[nx][ny] == 'O':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return count


# I(도연이) 위치 판단
x, y = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            x, y = i, j
res = bfs(x, y)
if res:
    print(res)
else:
    print('TT')
