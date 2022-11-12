from sys import stdin, stdout
input = stdin.readline


# num(A, B 합집합) - num(A, B 교집합)의 개수 구하기
a_num, b_num = map(int, input().split())
a_arr = list(map(int, input().split()))  # A 배열 입력
b_arr = list(map(int, input().split()))  # B 배열 입력
union_arr = set(a_arr + b_arr)  # 합집합 구하기
answer = a_num + b_num - 2*(len(a_arr + b_arr) - len(union_arr))
stdout.write(str(answer))