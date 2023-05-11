n, r, c = map(int, input().split())
# 0부터 시작, 4사분면으로 나뉜 section에 대해서 계속 4 sector로 나눠보면서 몇 번째인지 구하기
# 즉 x, y축에 대해서 각각 이분탐색 쭈욱 진행


lx, rx, ly, ry = 0, 2**n - 1, 0, 2**n - 1  # 초기 설정: 가로와 세로의 양 끝
lres, rres = 0, 2**(2*n)-1  # 초기 설정: 몇 번째인지 체크할 수 있는 양 끝
answer = 0
while True:
    x_pivot, y_pivot = (lx + rx) // 2, (ly + ry) // 2
    dif_per_dimen = (rres - lres + 1) // 4
    if r == x_pivot and c == y_pivot and lres == rres:  # 목적지에 도착했고 lres와 rres가 같을 때(만 정답)
        answer = lres
        break
    if r <= x_pivot and c > y_pivot:  # 1사분면
        rx, ly = x_pivot, y_pivot + 1
        lres, rres = lres + dif_per_dimen, rres - 2*dif_per_dimen
    elif r > x_pivot and c > y_pivot:  # 2사분면
        lx, ly = x_pivot + 1, y_pivot + 1
        lres = lres + 3*dif_per_dimen
    elif r > x_pivot and c <= y_pivot:  # 3사분면
        lx, ry = x_pivot + 1, y_pivot
        lres, rres = lres + 2*dif_per_dimen, rres - dif_per_dimen
    else:  # 4사분면
        rx, ry = x_pivot, y_pivot
        rres = rres - 3*dif_per_dimen
print(answer)
