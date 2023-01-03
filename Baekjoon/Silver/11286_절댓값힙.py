import sys
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline
n = int(input())


# n의 최대가 100,000이므로 시간복잡도 O(nlogn)으로 해결
queue = PriorityQueue()
answer = ''
for i in range(n):  # input이 0이면 최소 절대값 출력, 0이 아니면 배열에 x push
    command = int(input())
    if command == 0:
        if queue.empty():
            answer += '0\n'
        else:
            tmp = queue.get()
            answer += (str(tmp[1]) + '\n')  # tmp[1]을 통해, 원래 값을 출력하도록 함
    else:
        queue.put((abs(command), command))  # 절대값 우선 정렬, 절대값이 같은 경우 원래 값 순으로 정렬
sys.stdout.write(answer)
