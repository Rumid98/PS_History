import sys
input = sys.stdin.readline


# 소수 배열 생성
prime = [True for _ in range(1_000_001)]
prime[0], prime[1] = False, False
for i in range(3, 1001, 2):
    if prime[i]:
        for j in range(i*i, 1_000_001, i):
            prime[j] = False
n = int(input())
while n != 0:
    for i in range(3, n, 2):
        if prime[i] and prime[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
    n = int(input())
