from sys import stdin, stdout
input = stdin.readline
answer = 0


n = int(input())  # 입력받을 수의 길이
for x in list(input().strip()):  # 코드 압축
    answer += int(x)  # 입력 받은 value는 string이므로, int 변환을 해준다
stdout.write(str(answer))
