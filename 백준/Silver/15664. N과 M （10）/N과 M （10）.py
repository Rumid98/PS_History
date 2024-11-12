import sys
from itertools import combinations
input = sys.stdin.readline


n, m = map(int, input().split())
result = sorted(list(set([tuple(sorted(item)) for item in list(combinations(list(map(int, input().split())), m))])))
for item in result:
    for x in item:
        print(x, end=' ')
    print()
