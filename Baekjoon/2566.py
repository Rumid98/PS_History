from sys import stdin, stdout
input = stdin.readline


# 9x9 격자판에 총 81개의 숫자 입력
graph = [list(map(int, input().split())) for _ in range(9)]
answer, x, y = -1, 0, 0
# 탐색 시작
for i in range(9):
    for j in range(9):
        if graph[i][j] > answer:  # 현재 탐색 값이 저장된 answer 값보다 클 때
            answer, x, y = graph[i][j], i+1, j+1
print(answer)
print(x, y)