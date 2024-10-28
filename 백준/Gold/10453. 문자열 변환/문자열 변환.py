import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    A, B = input().split()
    A_array, B_array = [], []
    answer = 0
    if len(A) != len(B):
        print(-1)
        break
    for i in range(len(A)):
        if A[i] == 'a':
            A_array.append(i)
        if B[i] == 'a':
            B_array.append(i)
    if len(A_array) != len(B_array):
        print(-1)
        break
    for i in range(len(A_array)):
        answer += abs(A_array[i] - B_array[i])
    print(answer)
