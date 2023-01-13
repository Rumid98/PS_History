import sys
import heapq
input = sys.stdin.readline
n = int(input())
queue = []
for i in range(n):
    heapq.heappush(queue, int(input()))


answer = 0
while queue:
    if len(queue) == 1:  # 남은 수의 개수가 1개
        answer += heapq.heappop(queue)
    else:  # 그 이상
        a = heapq.heappop(queue)  # 첫 번째 숫자 뽑음 -> 이 숫자가 0인 경우, 두 번째 뽑을 숫자는 0 이상이므로, 고려 x
        if a < 0:  # 움수인 경우
            b = heapq.heappop(queue)  # 두 번째 숫자 뽑음 -> 0인 경우에는 합이 0이 되므로 필요 x
            if b < 0:  # 음수인 경우
                answer += (a * b)
            elif b > 0:  # 양수인 경우
                answer += a
                heapq.heappush(queue, b)
        elif a == 1:  # 1인 경우
            answer += a
        elif a > 1:  # 2 이상의 자연수인 경우
            if len(queue) % 2 == 0:  # 남은 수의 개수가 짝수
                answer += a
            else:  # 남은 수의 개수가 홀수
                answer += (a * heapq.heappop(queue))
sys.stdout.write(str(answer))
