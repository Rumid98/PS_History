def recursion(n, m, res):
    if m == 0:
        return res
    else:
        return recursion(n, m-1, res*n)


for _ in range(10):
    test_case = int(input())
    n, m = map(int, input().split())
    print(f'#{test_case} {recursion(n, m, 1)}')
