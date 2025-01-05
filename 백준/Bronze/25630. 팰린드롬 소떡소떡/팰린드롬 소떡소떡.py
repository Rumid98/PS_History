import sys
input = sys.stdin.readline


n = int(input())
input_string = input().strip()
answer = 0
for i in range(n//2):
    if input_string[i] != input_string[n-1-i]:
        answer += 1
print(answer)
