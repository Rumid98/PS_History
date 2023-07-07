from collections import deque
a, b = map(int, input().split())
count = 0


# b를 나누고, 1을 잘라서 a를 만드는 방향으로 진행
while True:
    if b == a:  # b와 a가 같아진 경우
        break
    elif b < a:  # b가 a보다 작아진 경우
        count = -1
        break

    if b % 2 == 0:  # b가 짝수인 경우
        b //= 2
        count += 1
    elif b % 10 == 1:  # b의 1의 자리가 1인 경우
        b //= 10
        count += 1
    else:  # 위의 두 경우에 속하지 않는 경우
        count = -1
        break
        
print(count + 1) if count != -1 else print(count)
