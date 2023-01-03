import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))


# n의 최대 크기가 1,000,000이므로, 시간복잡도 O(n)으로 해결
stack = []
answer = [-1] * n
# idx = 0  # nums의 숫자를 가져오기 위한 index 변수
for i in range(n):
    # stack이 비어있지 않고, stack 맨 위의 수가 현재 수보다 작은 경우 pop, 현재 수 저장
    while stack and stack[-1][1] < nums[i]:
        answer[stack[-1][0]] = nums[i]
        stack.pop()
    stack.append((i, nums[i]))  # stack에 [index, value]형태로 push
for i in range(n):
    sys.stdout.write(str(answer[i]) + ' ')
