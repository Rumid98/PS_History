import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    answer = []
    indegree = [0] * (n+1)
    for _ in range(m):
        tmp = list(map(int, input().split()))
        k, nums = tmp[0], tmp[1:]
        for i in range(k-1):
            graph[nums[i]].append(nums[i+1])
            indegree[nums[i+1]] += 1
    queue = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        cur = queue.popleft()
        answer.append(cur)
        for v in graph[cur]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    if len(answer) < n:
        print(0)
    else:
        print(*answer, sep='\n')


if __name__ == "__main__":
    main()
