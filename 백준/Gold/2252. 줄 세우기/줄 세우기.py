import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1

    def topology_sort():
        result = []
        queue = deque()
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            cur = queue.popleft()
            result.append(cur)
            for i in graph[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
        for x in result:
            print(x, end=' ')

    topology_sort()


if __name__ == "__main__":
    main()
