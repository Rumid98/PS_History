def solution(s):
    answer = ''
    checked = True
    for x in s:
        if x == ' ':
            answer += x
            checked = True
        elif checked:
            answer += x.upper()
            checked = False
        else:
            answer += x.lower()
            checked = False
    return answer