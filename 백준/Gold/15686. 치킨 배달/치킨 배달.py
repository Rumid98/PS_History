import sys
from itertools import combinations
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
chickens = []
houses = []
answer = 100_000_000
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append([i, j])
        if graph[i][j] == 2:
            chickens.append([i, j])
chicken_comb = list(combinations(chickens, m))
for chi_list in chicken_comb:
    result = 0
    for house in houses:
        tmp = 100_000_000
        for c in chi_list:
            tmp = min(tmp, abs(house[0]-c[0]) + abs(house[1]-c[1]))
        result += tmp
    answer = min(answer, result)
print(answer)
