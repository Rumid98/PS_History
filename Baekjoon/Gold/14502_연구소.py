import itertools
from collections import deque
import copy
n, m = map(int, input().split())  # 세로, 가로 크기
graph = [list(map(int, input().split())) for _ in range(n)]  # 연구소 지도 배열
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]
answer = 0
# 0: 빈칸, 1: 벽, 2: 바이러스
# 타일별로 넘버링(0 ~ n*m-1번) / 3개 선택 후 0을 1로 바꾼 후 탐색 진행


def bfs(lab):
    count = 0
    queue = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]  # 방문 배열
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 2:
                queue.append((i, j))  # 모든 바이러스 존재하는 칸 queue에 삽입
                visited[i][j] = True

    while queue:
        cur = queue.popleft()
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                lab[nx][ny] = 2
                queue.append((nx, ny))
    # bfs 진행 후 0인 칸 개수 세기
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                count += 1
    return count  # 0인 칸 개수 반환


zero_tile = []
for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            zero_tile.append(i*m + j)
possible_wall = list(itertools.combinations(zero_tile, 3))  # 벽 3개 놓을 수 있는 모든 가능한 조합
for i in range(len(possible_wall)):
    for j in range(3):
        graph[possible_wall[i][j] // m][possible_wall[i][j] % m] = 1  # 해당 위치 벽으로 바꿈
    tmp_graph = copy.deepcopy(graph)
    answer = max(answer, bfs(tmp_graph))  # bfs 반환값과 비교
    for j in range(3):
        graph[possible_wall[i][j] // m][possible_wall[i][j] % m] = 0  # 해당 위치 원상복귀
print(answer)
