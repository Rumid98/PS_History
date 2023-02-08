def solution(s):
    answer = []
    count_1, count_2 = 0, 0
    while s != '1':
        tmp = ''
        for x in s:  # 1만 남기는 과정
            if x == '1':
                tmp += x
            else:
                count_2 += 1
        s = str(bin(len(tmp)))[2:]
        count_1 += 1
    answer.append(count_1)
    answer.append(count_2)
    return answer