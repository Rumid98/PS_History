import sys
from collections import deque
input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
# f: 건물 전체 층
# s: 현재 층
# g: 목표 층
# u: 위로 u층 가는 버튼
# d: 아래로 d층 가는 버튼
startlink = [0] * (f+1)
visited = [False] * (f+1)


# 최대 층이 1,000,000이라 시간복잡도 걱정x, dp 진행
def bfs():
    queue = deque()
    queue.append(s)  # s 지점부터 탐색 시작
    visited[s] = True  # 방문 처리
    while queue:
        cur = queue.popleft()
        if cur == g:  # 목표지점에 도달한 경우
            break
        else:
            if 1 <= cur+u <= f and not visited[cur+u]:  # 현재 지점에서 위로 가는 경우
                startlink[cur+u] = startlink[cur] + 1
                queue.append(cur+u)
                visited[cur+u] = True
            if 1 <= cur-d <= f and not visited[cur-d]:  # 현재 지점에서 아래로 가는 경우
                startlink[cur-d] = startlink[cur] + 1
                queue.append(cur-d)
                visited[cur-d] = True


bfs()
if s == g:
    sys.stdout.write('0\n')
else:
    if startlink[g] != 0 and visited[g]:
        sys.stdout.write(str(startlink[g]))
    else:
        sys.stdout.write('use the stairs')
