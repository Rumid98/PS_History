import sys
input = sys.stdin.readline
nums = list(map(int, input().split()))
a, b = min(nums), max(nums)


while b > 1:
    if b % a == 0:
        break
    else:
        b, a = a, b % a
for i in range(a):
    sys.stdout.write('1')
