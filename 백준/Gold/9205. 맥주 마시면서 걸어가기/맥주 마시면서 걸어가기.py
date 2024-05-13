import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = [list(map(int, input().split())) for _ in range(n+2)]
        graph = [[] for _ in range(n+2)]  # 0: 출발지, 1~n: 편의점 위치, n+1: 페스티벌 위치
        visited = [False] * (n+2)
        result = False
        for i in range(n+2):
            for j in range(n+2):
                if i != j:
                    if abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) <= 1000:
                        graph[i].append(j)
                        graph[j].append(i)
        queue = deque()
        queue.append(0)
        while queue:
            cur = queue.popleft()
            if cur == n+1:
                result = True
                break
            for node in graph[cur]:
                if not visited[node]:
                    visited[node] = True
                    queue.append(node)
        print('happy') if result else print('sad')


if __name__ == "__main__":
    main()
