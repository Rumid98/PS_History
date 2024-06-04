import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 1:
                queue = deque()
                queue.append([i, j])
                visited = [[False] * m for _ in range(n)]
                visited[i][j] = True
                end = False
                count = 0
                while queue:
                    q_len = len(queue)
                    for _ in range(q_len):
                        cur = queue.popleft()
                        if graph[cur[0]][cur[1]] == 1 and count != 0:
                            end = True
                            break
                        for k in range(8):
                            nx, ny = cur[0] + dx[k], cur[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                                queue.append([nx, ny])
                                visited[nx][ny] = True
                    if end:
                        break
                    count += 1
                answer = max(answer, count)
    print(answer)


if __name__ == "__main__":
    main()
