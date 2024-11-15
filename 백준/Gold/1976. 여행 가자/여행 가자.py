import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


n = int(input())
m = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
parent = [i for i in range(n+1)]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parent[b] = a
    
def find(v):
    if v == parent[v]:
        return v
    else:
        parent[v] = find(parent[v])
        return parent[v]

for i in range(n):
    for j in range(i+1, n):
        if info[i][j] == 1:
            union(i+1, j+1)
cities = list(map(int, input().split()))
city = find(cities[0])
for x in cities[1:]:
    if find(x) != city:
        print('NO')
        break
else:
    print('YES')
