n = int(input())
nums = list(map(int, input().split()))
x, y = map(int, input().split())


# 상대평가일 경우
print(int(len(nums)*x/100), end=' ')
# 절대평가인 경우
count = 0
for i in nums:
    if i >= y:
        count += 1
print(count)
