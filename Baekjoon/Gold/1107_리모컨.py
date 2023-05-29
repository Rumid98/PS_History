import itertools


n = int(input())  # 이동하려는 채널  /  현재 보고있는 채널은 100
k = int(input())  # 고장난 버튼의 수
original_button = [i for i in range(10)]  # 0~9까지 버튼
broken_button = []
available_button = []  # 누를 수 있는 버튼, str 형태로 저장
if k:  # 고장난 버튼이 0개가 아닌 경우
    broken_button = list(map(int, input().split()))  # 고장난 버튼 정보
for i in range(10):
    if i not in broken_button:
        available_button.append(str(i))

minimum_dif = abs(n-100)  # 100번에서 + 또는 -로 갈 수 있는 횟수를 초기값으로
for i in range(1, 7):
    tmp_list = list(itertools.product(available_button, repeat=i))
    for x in tmp_list:
        num = ''.join(x)
        minimum_dif = min(minimum_dif, len(num) + abs(int(num)-n))  # 숫자 길이에 + 혹은 - 누른 횟수
print(minimum_dif)
