def solution(price, money, count):
    answer = 0
    tmp = 0
    for i in range(1, count + 1):
        tmp += i
    if price * tmp > money:
        answer = price * tmp - money
    return answer