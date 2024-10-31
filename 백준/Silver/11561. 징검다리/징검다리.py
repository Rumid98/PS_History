import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    n = int(input())
    answer = 1
    lt, rt = 1, 10 ** 10
    while lt <= rt:
        pivot = (lt + rt) // 2
        tmp = pivot * (pivot + 1) // 2
        if tmp > n:
            rt = pivot - 1
        else:
            answer = pivot    
            lt = pivot + 1
    print(answer)
