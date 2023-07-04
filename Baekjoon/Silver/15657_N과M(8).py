import itertools
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
answer = list(itertools.combinations_with_replacement(nums, m))
for com in answer:
    for x in com:
        print(x, end=' ')
    print()
