import itertools
n, m = map(int, input().split())
answer = list(itertools.combinations([i for i in range(1, n+1)], m))
for com in answer:
    for x in com:
        print(x, end=' ')
    print()
