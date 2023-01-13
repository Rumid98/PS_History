import sys
import heapq
input = sys.stdin.readline
command = input().strip()


# '-' 부호 기준으로 나눈다. 왜냐면 -부터 다음 -까지 그 사이 숫자는 괄호처리 해서 전부 빼주기 때문
answer = 0
split_by_minus = list(command.split('-'))
for i in range(len(split_by_minus)):
    if i == 0:
        answer += sum(list(map(int, split_by_minus[i].split('+'))))
    else:
        answer -= sum(list(map(int, split_by_minus[i].split('+'))))
sys.stdout.write(str(answer))
