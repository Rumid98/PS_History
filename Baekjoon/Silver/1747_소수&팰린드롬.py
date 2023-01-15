import sys
input = sys.stdin.readline
n = int(input())


# 소수
p = [True] * (1003002)
p[0], p[1] = False, False
for i in range(2, 1003002):
    if p[i]:
        for j in range(i*i, 1003002, i):
            p[j] = False
# n 이상인 소수 중에서 팰린드롬인 수
for i in range(n, 1003002):
    if p[i]:
        check = True
        palin = str(i)
        palin_len = len(palin)
        for j in range(palin_len//2):  # 절반의 index만으로 대칭 판별
            if palin[j] != palin[palin_len - j - 1]:
                check = False
        if check:
            sys.stdout.write(palin)
            break
