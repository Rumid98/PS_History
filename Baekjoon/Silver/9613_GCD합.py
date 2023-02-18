import sys
input = sys.stdin.readline


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


t = int(input())
for _ in range(t):
    nums = list(map(int, input().split()))  # list의 index 0에는 n, 1부터는 해당 숫자들이 존재
    n = nums[0]
    answer = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            answer += gcd(nums[i], nums[j])
    sys.stdout.write(str(answer) + '\n')
