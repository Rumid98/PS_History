import sys
import heapq
input = sys.stdin.readline
n = int(input())
coun = [list(map(int, input().split())) for _ in range(n)]


# 회의가 끝나야만 다음 회의를 진행할 수 있음
# 끝나는 시간이 빠른 순으로 정렬하되, 시작 시간이 이른 순으로 정렬
coun.sort(key=lambda x: x[0])
coun.sort(key=lambda x: x[1])
answer = 0
cur = 0
for i in range(n):
    if coun[i][0] >= cur:
        answer += 1
        cur = coun[i][1]
sys.stdout.write(str(answer))
