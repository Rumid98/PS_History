nA, nB = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
res = []


idxA, idxB = 0, 0
while idxA < nA and idxB < nB:  # index 범위 안
    if A[idxA] < B[idxB]:  # A 값이 작은 경우
        res.append(A[idxA])
        idxA += 1
    elif A[idxA] == B[idxB]:  # 같은 경우
        idxA += 1
        idxB += 1
    else:  # A 값이 큰 경우
        idxB += 1
while idxA < nA:  # 나머지 값(존재할 경우) 채워넣기
    res.append(A[idxA])
    idxA += 1
if not res:
    print(0)
else:
    print(len(res))
    for x in res:
        print(x, end=' ')
