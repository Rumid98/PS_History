import sys
input = sys.stdin.readline
m, n = map(int, input().split())
answer = 0


# 에라토스테네스의 체를 이용한 소수 판별
maxi = int(n**(1/2)) + 1
almost = []
p = [True] * (maxi + 1)
p[0], p[1] = False, False
for i in range(2, maxi + 1):
    if p[i]:
        almost.append(i)
        for j in range(i * i, maxi + 1, i):
            p[j] = False
# 소수에 대해서만 탐색 진행
for x in almost:
    count = 2  # 2제곱부터 시작
    while True:
        if x ** count > n:  # n제곱이 B보다 커진 경우 break
            break
        if x ** count >= m:  # 그 외, n제곱이 A 이상인 경우
            answer += 1
        count += 1
sys.stdout.write(str(answer))
