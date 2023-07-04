import itertools
n, m = map(int, input().split())
answer = list(itertools.combinations_with_replacement([i for i in range(1, n+1)], m))
itertools.product()
for com in answer:
    for x in com:
        print(x, end=' ')
    print()
