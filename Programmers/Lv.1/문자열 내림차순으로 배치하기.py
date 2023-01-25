def solution(s):
    answer = ''
    al = list(s)
    al.sort(reverse=True)
    for x in al:
        answer += x
    return answer