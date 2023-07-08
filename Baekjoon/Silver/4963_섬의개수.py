from collections import deque
dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        cur = queue.popleft()
        for i in range(8):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    answer = 0
    graph = [list(map(int, input().split())) for _ in range(h)]  # 1: 땅, 0: 바다
    visited = [[False for _ in range(w)] for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                answer += 1
    print(answer)
