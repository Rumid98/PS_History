import sys
input = sys.stdin.readline


# 무조건 dp / 10^6 = 1_000_000
d = [0 for _ in range(1_000_001)]
n = int(input())
for i in range(2, n+1):
    d[i] = d[i-1] + 1  # 3번 조건에 해당
    if i % 2 == 0:  # 2번 조건에 해당
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:  # 1번 조건에 해당
        d[i] = min(d[i], d[i//3] + 1)
sys.stdout.write(str(d[n]))
