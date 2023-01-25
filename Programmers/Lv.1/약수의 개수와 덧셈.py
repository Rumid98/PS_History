def solution(left, right):
    answer = 0
    sqr = []
    for i in range(1, 32):
        sqr.append(i*i)
    for i in range(left, right+1):
        if i in sqr:
            answer -= i
        else:
            answer += i
    return answer