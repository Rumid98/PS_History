import sys
from collections import deque
input = sys.stdin.readline
n, m, b = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]  # 마인크래프트 땅 입력
answer_time, answer_height = 1_000_000_000, 0


# n, m은 최대 500, 최대 총 25,000 개 탐색 / 땅의 높이는 256이하  -->  최대 6,400,000개
for i in range(257):  # 높이를 0 ~ 256으로 맞춰보는 탐색
    count = 0  # 걸리는 시간 체크
    tmp = b  # 임시 블럭 개수
    for j in range(n):
        for k in range(m):  # 입력받은 넓이 전체 탐색
            cur = graph[j][k]
            if cur > i:  # 1번 작업에 해당
                count += 2*(cur - i)
                tmp += (cur - i)
            elif cur < i:  # 2번 작업에 해당
                count += (i - cur)
                tmp -= (i - cur)
    if tmp >= 0 and count <= answer_time:  # 블럭이 모자라지 않았고, 최소시간인 경우
        answer_time, answer_height = count, i
sys.stdout.write(str(answer_time) + ' ' + str(answer_height))
