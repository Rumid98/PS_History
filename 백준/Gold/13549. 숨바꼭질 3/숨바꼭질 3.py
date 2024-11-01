import sys
import heapq
input = sys.stdin.readline


n, k = map(int, input().split())
queue = []
visited = [False] * 100_001
heapq.heappush(queue, [0, n])

while queue:
    cur_count, cur_node = heapq.heappop(queue)
    if cur_node == k:
        print(cur_count)
        break
    if visited[cur_node]:
        continue
    visited[cur_node] = True
    if cur_node * 2 <= 100_000:
        heapq.heappush(queue, [cur_count, cur_node*2])
    if cur_node - 1 >= 0:
        heapq.heappush(queue, [cur_count+1, cur_node-1])
    if cur_node + 1 <= 100_000:
        heapq.heappush(queue, [cur_count+1, cur_node+1])
