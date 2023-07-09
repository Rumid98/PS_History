str = input()
answer = ''
idx = 0
str_len = len(str)
bracket = False
tmp = []

while idx < str_len:
    if str[idx] == ' ':  # 공백 처리
        if tmp:
            tmp.reverse()
            for x in tmp:
                answer += x
            tmp = []
        answer += str[idx]
    elif str[idx] == '<':  # < 처리
        if tmp:
            tmp.reverse()
            for x in tmp:
                answer += x
            tmp = []
        answer += str[idx]
        bracket = True
    elif str[idx] == '>':  # > 처리
        answer += str[idx]
        bracket = False
    else:  # 숫자, 알파벳 처리
        if bracket:  # <> 안의 내용
            answer += str[idx]
        else:  # <> 이외의 내용
            tmp.append(str[idx])
    idx += 1
if tmp:
    tmp.reverse()
    for x in tmp:
        answer += x
    tmp = []

print(answer)

