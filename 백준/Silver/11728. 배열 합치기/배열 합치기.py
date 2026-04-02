import sys
input = sys.stdin.readline


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

i, j = 0, 0
answer = []
while i < N and j < M:
    if A[i] < B[j]:
        answer.append(A[i])
        i += 1
    else:
        answer.append(B[j])
        j += 1

if i != N:
    answer += A[i:]
else:
    answer += B[j:]

for i in range(N + M):
    print(answer[i], end=' ')