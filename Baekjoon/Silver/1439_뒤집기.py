def find(s):  # c: 찾고자 하는 char, s: 입력받은 문자열
    start_c = s[0]
    idx = 0
    result = 0
    while idx != len(s):
        if s[idx] == start_c:  # 찾고자 하는 값이면
            idx += 1
        else:  # 다른 값이면
            while idx != len(s) and s[idx] != start_c:
                idx += 1  # index는 계속 증가
            result += 1
    return result


string = input().strip()
print(find(string))
