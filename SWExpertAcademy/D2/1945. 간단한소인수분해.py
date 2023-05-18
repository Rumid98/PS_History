T = int(input())
answer = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    p_num = [2, 3, 5, 7, 11]
    res = f'#{test_case} '

    def fun(n, p):
        count = 0
        while True:
            if n % p != 0:
                break
            n //= p
            count += 1
        return count

    for i in range(5):
        res += (str(fun(n, p_num[i])) + ' ')
    answer.append(res)
print('\n'.join(answer))
