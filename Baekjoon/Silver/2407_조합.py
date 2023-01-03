import sys
input = sys.stdin.readline
n, m = map(int, input().split())


a, b, c = 1, 1, 1
for i in range(1, n + 1):
    a *= i
for i in range(1, m + 1):
    b *= i
for i in range(1, n - m + 1):
    c *= i
sys.stdout.write(str(a // (b * c)))
