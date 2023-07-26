import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):  # test case 만큼 loop
    n = int(input())
    if n == 0:  # 의상 개수가 0인 경우(알몸 상태만 가능)
        print(0)
    else:
        clothes = {}  # 의상 종류별 의상 개수 저장 dictionary - {type: [x1, x2, ...]} 형태
        answer = 1
        for i in range(n):  # 의상의 수만큼 loop 진행
            c_name, c_type = input().split()
            if c_type not in clothes:
                clothes[c_type] = [c_name]  # list 형태가 되도록 삽입
            else:
                clothes[c_type].append(c_name)
        c_keys = list(clothes.keys())  # 의상의 종류 list로 return
        for key in c_keys:
            answer *= (len(clothes[key]) + 1)  # 0~n개이므로 +1 해줌
        print(answer - 1)  # 전체 가능한 경우에서 알몸 상태인 경우 한 가지 제외
