import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
t = int(input())  # test case 개수 입력
answer = ''  # 출력값 저장 변수


# 해당 수를 1, 2, 3의 합으로 나타낼 수 있는 방법의 수
D = [0] * 11  # 정수 합 저장 배열
D[1] = 1
D[2] = 2
D[3] = 4
for i in range(4, 11):  # 2부터 10까지 합 저장
    D[i] = D[i-1] + D[i-2] + D[i-3]
for i in range(t):  # test case 만큼 답 입력 진행
    n = int(input())
    answer += str(D[n]) + '\n'

sys.stdout.write(answer)
