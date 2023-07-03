n = int(input())
m = int(input())
str = input().strip()
answer = 0

idx = 0  # 현재 idx를 나타낼 변수
pre = str[0]  # 현재 idx에 대해서, 이전 idx 알파벳 저장할 변수
IOI = []
while idx < m-1:
    changed = True
    if str[idx] == 'I':  # I인 경우에 탐색 시작
        count = 1
        while idx < m-1 and changed:
            if str[idx] != str[idx+1]:
                count += 1
            else:  # 안바뀌었다면
                changed = False  # False, 반복문 탈출
            idx += 1
        if count > 1:
            IOI.append(count)
    else:  # 'I'가 아닌 경우에 그냥 idx+1 진행
        idx += 1
for x in IOI:
    if (x - 1) // 2 - n + 1 > 0:
        answer += ((x - 1) // 2 - n + 1)
print(answer)
