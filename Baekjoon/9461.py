from sys import stdin, stdout
input = stdin.readline


# 파도반 수열 -> 6번째 삼각형부터 규칙이 나타남 : D[n] = D[n-1] + D[n-5]
t = int(input())  # test case 개수 입력
answer = ''  # 정답 저장
D = [0] * 101  # D[5]까지는 특별한 규칙이 없어, 따로 저장
D[1] = D[2] = D[3] = 1
D[4] = D[5] = 2
for i in range(6, 101):  # 규칙대로 점화식을 세워준다
    D[i] = D[i-1] + D[i-5]
for i in range(t):
    n = int(input())
    answer += str(D[n]) + '\n'
stdout.write(answer)
