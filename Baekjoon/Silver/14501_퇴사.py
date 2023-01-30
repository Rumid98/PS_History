import sys
input = sys.stdin.readline
n = int(input())  # n일 입력
graph = [list(map(int, input().split())) for _ in range(n)]  # 1일차 ~ n일차 상담 기간 + 수익 저장 배열
d = [0] * (n + 1)  # dp 배열


for i in range(n-1, -1, -1):  # dp 탐색은 뒤에서부터 앞으로 진행
    t, p = graph[i][0], graph[i][1]  # (i+1)번째 날 상담의 소요시간 t와 수익 p
    if i + t <= n:  # 상담이 퇴사 전까지 종료되는 경우
        d[i] = max(d[i+1], d[i+t] + p)  # 직후 날짜 수익과 상담을 진행했을 때의 수익 중 큰 값을 대입
    else:  # 상담이 퇴사 전까지 종료되지 않는 경우
        d[i] = d[i+1]  # 직후 날짜 수익 그대로 가져옴
sys.stdout.write(str(d[0]))
