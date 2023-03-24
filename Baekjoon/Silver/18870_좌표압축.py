import sys
import heapq
input = sys.stdin.readline


# 데이터 개수 최대 1_000_000개(백만개)
n = int(input())
nums = list(map(int, input().split()))
answer = [0 for _ in range(n)]
queue = []  # heap으로 사용할 queue 선언
count = 0  # 이전 값 count 변수 선언
mini = min(nums)  # heap을 이용하여 최솟값부터 탐색할 예정이므로 시작값을 최솟값으로 설정

# heap에 숫자 집어넣기
for i in range(n):
    heapq.heappush(queue, (nums[i], i))  # (입력값, 인덱스) 형태로 힙에 삽입
# 정답 배열 완성
for _ in range(n):
    cur_num, cur_idx = heapq.heappop(queue)
    if cur_num > mini:
        count += 1
        answer[cur_idx] = count
        mini = cur_num
    else:
        answer[cur_idx] = count
# 정답 출력
for num in answer:
    sys.stdout.write(str(num) + ' ')
