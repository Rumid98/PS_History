n = int(input())


# n은 최대 1,000,000
result = 1
for i in range(1, n+1):
    result *= i
    while True:  # 끝에 0 항상 제거
        if result % 10 == 0:
            result //= 10
        else:
            break
    result %= 100_000_000_000_000  # 너무 큰 수가 되지 않게 해준다
print(str(result)[-5:])
