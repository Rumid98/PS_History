import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def union(a, b):
    a_parent, b_parent = find(a), find(b)
    if a_parent <= b_parent:
        nodes[b_parent] = a_parent
    else:
        nodes[a_parent] = b_parent

def find(v):
    if v == nodes[v]:
        return v
    else:
        nodes[v] = find(nodes[v])
        return nodes[v]

n, m = map(int, input().split())
nodes = [i for i in range(n+1)]
for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)
    else:
        print('YES') if find(a) == find(b) else print('NO')
