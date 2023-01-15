import sys
input = sys.stdin.readline
n = int(input())


count = n
for i in range(2, int(n**(1/2)) + 1):  # 제곱근까지만 진행
    if n % i == 0:
        count -= int(count / i)
        while n % i == 0:
            n /= i
if n > 1:
    count -= int(count/n)
sys.stdout.write(str(count))
