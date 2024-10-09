def factorial(a, b):
    result = 1
    for i in range(a, b):
        result *= i
        result %= p
    return result

n, p = map(int, input().split())
if n == p-1:
    answer = p-1
elif n > p - n:
    answer = factorial(n+1, p-1)
    answer = pow(answer, p-2, p)
else:
    answer = factorial(1, n+1)
print(answer)