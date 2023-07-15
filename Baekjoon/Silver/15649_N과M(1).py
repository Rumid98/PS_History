import itertools
n, m = map(int, input().split())
nums = [i for i in range(1, n+1)]

res = list(itertools.permutations(nums, m))
for r in res:
    for i in range(len(r)):
        print(r[i], end=' ')
    print()
