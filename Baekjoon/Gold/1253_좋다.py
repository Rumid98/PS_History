import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
answer = 0


# 수의 개수는 최대 2000개, 최악의 경우 2,000*2,000(총 4,000,000)이므로 sliding window로 진행
nums.sort()
for i in range(n):
    cur_idx = i
    left, right = 0, n-1
    while left < right:
        total = nums[left] + nums[right]
        if total == nums[i]:
            if left != i and right != i:
                answer += 1
                break
            elif left == i:
                left += 1
            elif right == i:
                right -= 1
        elif total > nums[i]:
            right -= 1
        else:
            left += 1
sys.stdout.write(str(answer))
