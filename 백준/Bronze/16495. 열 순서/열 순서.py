import sys
input = sys.stdin.readline


line = input().strip()
line_len = len(line)
answer = 0
for i in range(line_len):
    answer += (ord(line[line_len-i-1]) - ord('A') + 1) * (26**i)
print(answer)