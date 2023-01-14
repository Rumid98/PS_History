import sys
input = sys.stdin.readline
m, n = map(int, input().split())


# 에라토스테네스의 체를 이용한 소수 판별
p = [True] * (n + 1)
p[0], p[1] = False, False
for i in range(2, n + 1):
    if p[i]:
        for j in range(i * i, n + 1, i):
            p[j] = False
# m ~ n의 소수 출력
for i in range(m, n + 1):
    if p[i]:
        sys.stdout.write(str(i) + '\n')
