from sys import stdin, stdout
input = stdin.readline


# 입력받은 10x10 정사각형 색칠하는 함수
def painting(graph, a, b):
    for i in range(a, a+10):
        for j in range(b, b+10):
            graph[i][j] += 1


n = int(input())
answer = 0
graph = [[0]*100 for _ in range(100)]  # 100x100 도화지 선언
for i in range(n):
    a, b = map(int, input().split())  # x, y 축과의 거리 입력
    painting(graph, a, b)  # 각 경우별로 색칠
for i in range(100):
    for j in range(100):
        if graph[i][j] != 0:  # 한 번이라도 색칠 된 경우
            answer += 1
stdout.write(str(answer))
