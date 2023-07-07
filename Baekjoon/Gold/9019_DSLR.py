from collections import deque
import sys
imput = sys.stdin.readline
t = int(input())  # 테스트케이스 개수 입력


for _ in range(t):
    a, b = map(int, input().split())  # a, b 입력 / 모두 0 ~ 9999 범위의 정수
    queue = deque()
    visited = [False for _ in range(10000)]  # 0~9999 숫자만 체크
    queue.append((a, ''))  # (십진수, 명령어) 형태로 queue에 저장
    visited[a] = True

    while queue:
        cur_node, path = queue.popleft()
        if cur_node == b:
            print(path)
            break

        nx = (2 * cur_node) % 10000
        if not visited[nx]:
            visited[nx] = True
            queue.append((nx, path + 'D'))

        nx = cur_node - 1 if cur_node != 0 else 9999
        if not visited[nx]:
            visited[nx] = True
            queue.append((nx, path + 'S'))

        nx = (cur_node % 1000) * 10 + (cur_node // 1000)
        if not visited[nx]:
            visited[nx] = True
            queue.append((nx, path + 'L'))

        nx = (cur_node % 10) * 1000 + (cur_node // 10)
        if not visited[nx]:
            visited[nx] = True
            queue.append((nx, path + 'R'))
