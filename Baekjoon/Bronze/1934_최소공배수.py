import sys
input = sys.stdin.readline
t = int(input())


for i in range(t):
    nums = list(map(int, input().split()))
    a, b = min(nums), max(nums)
    while b > 1:
        if b % a == 0:
            break
        else:
            b, a = a, b%a
    sys.stdout.write(str(nums[0]*nums[1]//a) + '\n')
