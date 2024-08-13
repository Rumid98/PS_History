import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    a, k = map(int, input().split())
    answer = 0
    queue = deque()
    queue.append([a, 0])
    visited = [False] * (k+1)
    visited[a] = True
    while queue:
        cur, count = queue.popleft()
        if cur == k:
            answer = count
            break
        if cur + 1 <= k and not visited[cur+1]:
            queue.append([cur+1, count+1])
            visited[cur+1] = True
        if cur * 2 <= k and not visited[cur*2]:
            queue.append([cur*2, count+1])
            visited[cur*2] = True
    print(answer)


if __name__ == "__main__":
    main()
