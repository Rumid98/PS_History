import sys
input = sys.stdin.readline


n = int(input())
buds = list(map(int, input().split()))
max_bud = int(input())

if sum(buds) <= max_bud:
    print(max(buds))
else:
    answer = 0
    m = len(buds)
    lt, rt = 0, 100_000
    while lt <= rt:
        pivot = (lt + rt) // 2
        tmp = 0
        for bud in buds:
            if bud > pivot:
                tmp += pivot
            else:
                tmp += bud
        if tmp <= max_bud:
            answer = pivot
            lt = pivot + 1
        else:
            rt = pivot - 1    
    print(answer)
