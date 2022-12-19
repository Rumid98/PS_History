import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0


# 수를 정렬할 필요가 없다. 입력받은 순서 그대로 search하여 부분합이 m인 경우를 찾는다.
lt, rt, total = 0, 1, nums[0]  # 합의 구간은 lt이상, rt미만이다.
while True:
    if total == m:
        answer += 1
        total -= nums[lt]
        lt += 1
    elif total > m:
        total -= nums[lt]
        lt += 1
    else:
        if rt < n:
            total += nums[rt]
            rt += 1
        else:
            break
sys.stdout.write(str(answer))
