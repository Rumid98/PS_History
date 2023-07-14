n = int(input())
d = [0 for _ in range(1001)]  # 0제외, 1~n까지 탐색
d[1] = 1
d[2] = 3  # 2x2 한 개로도 채울 수가 있다.
for i in range(3, n+1):
    d[i] = d[i-1] + 2*d[i-2]
print(d[n] % 10007)
