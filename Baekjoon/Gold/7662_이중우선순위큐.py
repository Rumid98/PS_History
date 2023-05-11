import heapq
import sys
input = sys.stdin.readline  # 이거 안 해서 시간초과


answer = []
t = int(input())  # 테스트케이스 개수
for _ in range(t):
    n = int(input())  # 명령 개수
    max_heap = []
    min_heap = []
    visited = [False for _ in range(1_000_001)]
    for i in range(n):
        command = input().strip()
        if command[0] == 'I':  # 입력인 경우
            heapq.heappush(max_heap, (-int(command[2:]), i))
            heapq.heappush(min_heap, (int(command[2:]), i))
            visited[i] = True  # 삽입하는 수에 i라는 key값을 부여한 채로 넣음
        else:  # 삭제인 경우
            if command[2] == '1':  # max값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:  # min값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    if max_heap and min_heap:
        answer.append(f'{-max_heap[0][0]} {min_heap[0][0]}')
    else:
        answer.append('EMPTY')
print('\n'.join(answer))
