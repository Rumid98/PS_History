import sys
import copy
from collections import deque
def input(): return sys.stdin.readline().strip()
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
answer = 0


def main():
    graph = [[] for _ in range(4)]
    direction = [[] for _ in range(4)]
    for i in range(4):
        line = list(map(int, input().split()))
        for j in range(8):
            if j % 2 == 0:
                graph[i].append(line[j])
            else:
                direction[i].append(line[j])
    DFS(graph, direction,0, 0, 0)
    print(answer)


def DFS(graph, direction, x, y, count):
    global answer
    g = copy.deepcopy(graph)
    d = copy.deepcopy(direction)
    count += g[x][y]
    g[x][y] = -1  # 매 단계 첫 번째는 현재 상어 위치의 물고기가 잡아먹힘
    # 1. 물고기 이동
    for fish in range(1, 17):
        end = False
        for i in range(4):
            for j in range(4):
                if g[i][j] == fish:
                    init_dir = d[i][j]
                    for _ in range(8):
                        nx, ny = i + dx[init_dir], j + dy[init_dir]
                        if 0 <= nx < 4 and 0 <= ny < 4 and g[nx][ny] != -1:
                            g[i][j], g[nx][ny] = g[nx][ny], g[i][j]
                            d[i][j], d[nx][ny] = d[nx][ny], init_dir
                            break
                        init_dir = init_dir + 1 if init_dir < 8 else 1
                    end = True
                    break
            if end:
                break
    # 2. 상어 이동
    can_move = False
    for nn in range(4):
        nx, ny = x + nn*dx[d[x][y]], y + nn*dy[d[x][y]]
        if 0 <= nx < 4 and 0 <= ny < 4 and g[nx][ny] > 0:
            can_move = True
            g[x][y] = 0
            DFS(g, d, nx, ny, count)
    # 3. 상어 이동 불가능
    if not can_move:
        answer = max(answer, count)
        return


if __name__ == "__main__":
    main()
