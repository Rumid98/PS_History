from sys import stdin, stdout
input = stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))


nums.sort()
stdout.write(str(nums[k - 1]))
