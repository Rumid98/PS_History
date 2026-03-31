import sys
input = sys.stdin.readline


P, K = map(int, input().split())
p = [True] * (10**6+1)
p[0] = p[1] = False

for i in range(2, 10**6+1):
    if p[i]:
        for j in range(i*i, 10**6+1, i):
            p[j] = False

for i in range(2, K):
    if p[i]:
        if P % i == 0:
            print("BAD", i)
            break
else:
    print("GOOD")