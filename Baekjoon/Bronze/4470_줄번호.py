n = int(input())
answer = ''
for i in range(1, n + 1):
    input_line = input()
    answer += (str(i) + '. ' + input_line + '\n')
print(answer)