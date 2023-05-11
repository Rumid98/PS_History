import sys
sys.setrecursionlimit(10000)
n = int(input())  #
graph = [list(map(int, input().split())) for _ in range(n)]  # 색종이 정보 배열  / 0: 흰색, 1: 파란색
answer_white = 0
answer_blue = 0


def search(paper):
    global answer_white, answer_blue
    count = [0, 0]  # white, blue 종이 숫자 count 배열
    length = len(paper)
    if length == 1:  # 종료 조건
        if not paper[0][0]:  # white인 경우
            answer_white += 1
        else:
            answer_blue += 1
        return
    for i in range(length):
        for j in range(length):
            if paper[i][j] == 0:
                count[0] += 1
            else:
                count[1] += 1
    if count[0] and count[1]:  # 두 색 모두 존재하는 경우
        search([row[:length // 2] for row in paper[:length // 2]])
        search([row[:length // 2] for row in paper[length // 2:]])
        search([row[length // 2:] for row in paper[:length // 2]])
        search([row[length // 2:] for row in paper[length // 2:]])
    else:
        if count[0]:
            answer_white += 1
        else:
            answer_blue += 1


search(graph)
print(answer_white)
print(answer_blue)


