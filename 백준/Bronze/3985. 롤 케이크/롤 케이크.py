import sys
input = sys.stdin.readline


l = int(input())
n = int(input())
cakes = [0] * (l+1)
cake_exp = [0, 0]
cake_real = [0] * (n+1)

for i in range(1, n+1):
    a, b = map(int, input().split())
    if b-a+1 > cake_exp[0]:
        cake_exp = [b-a+1, i]
    for j in range(a, b+1):
        if cakes[j] == 0:
            cakes[j] = i
for i in range(l):
    cake_real[cakes[i]] += 1
max_real_value = max(cake_real[1:])
for i in range(1, n+1):
    if cake_real[i] == max_real_value:
        print(cake_exp[1])
        print(i)
        break
