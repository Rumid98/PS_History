import sys
from collections import deque
input = sys.stdin.readline
n, l = map(int, input().split())
nums = list(map(int, input().split()))
queue = deque()


# n의 최대가 5,000,000이므로, O(n^2) 또는 O(nlogn)인 경우 시간초과가 날 것이다. 반드시 O(n)으로 풀어야 한다.
for i in range(n):
    while queue and queue[-1][1] > nums[i]:  # 현재 value보다 deque에 들어있는 value가 클 경우, pop
        queue.pop()
    queue.append((i, nums[i]))  # deque에 (index, value) 형태, append
    if queue[0][0] <= i - l:  # 맨 앞 index가 슬라이딩 윈도우 범위를 벗아난 경우, popleft
        queue.popleft()
    sys.stdout.write(str(queue[0][1]) + ' ')
