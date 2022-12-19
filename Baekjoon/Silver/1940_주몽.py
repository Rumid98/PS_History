import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
nums = list(map(int, input().split()))
answer = 0


# 갑옷은 두 개의 재료로 만들어지는데, 그 합이 m일 경우만 가능하다(여러 숫자들 중 두 개만 match 시킨다)
# 숫자들을 정렬 후, start, end를 가운데로 이동시키면서 탐색
nums.sort()
start_idx, end_idx = 0, len(nums)-1
while start_idx < end_idx:
    gap = nums[start_idx] + nums[end_idx]
    if gap == m:
        answer += 1
        start_idx += 1
        end_idx -= 1
    elif gap > m:
        end_idx -= 1
    else:
        start_idx += 1
sys.stdout.write(str(answer))
