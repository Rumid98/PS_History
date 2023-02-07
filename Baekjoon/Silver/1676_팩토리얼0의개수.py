n = int(input())
answer = 0
fac = 1
for i in range(2, n+1):
    fac *= i
    while fac % 10 == 0:
        fac //= 10
        answer += 1
    if fac > 1_000_000:  # 너무 큰 수가 되지 않게
        fac %= 1_000_000
print(answer)
