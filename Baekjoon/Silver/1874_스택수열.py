import sys
input = sys.stdin.readline
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))


# n의 범위가 100,000이므로, O(nlogn)이하의 시간복잡도로 풀어야 함
answer = ''
stack = []
idx = 0  # nums 값 비교를 위한 idx 설정
for i in range(1, n+1):  # start=1, end=n
    stack.append(i)
    answer += '+\n'
    if stack[-1] == nums[idx]:  # stack 상단 값이 비교 대상(nums[idx])과 같은 경우
        stack.pop()
        idx += 1
        answer += '-\n'
        while stack and idx < n:  # 스택이 비었거나, idx가 끝에 도달했을 경우 break
            if nums[idx] == stack[-1]:
                stack.pop()
                idx += 1
                answer += '-\n'
            else:
                break
if idx == n:
    sys.stdout.write(answer)
else:
    sys.stdout.write("NO")
    