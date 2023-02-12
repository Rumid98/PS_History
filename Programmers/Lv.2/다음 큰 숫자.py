def solution(n):
    answer = 0
    count = str(bin(n)[2:]).count('1')
    for i in range(n+1, 1_000_000_000):
        if count == str(bin(i)[2:]).count('1'):
            answer = i
            break
    return answer