n = int(input())
statues = list(map(int, input().split()))


# 왼쪽인 경우 -1, 오른쪽인 경우 1을 더해서 배열합을 만들고, 배열합끼리 대조해서 가장 큰 값을 구해본다
paint = [0] * (n + 1)  # 0 인덱스 ~ k 인덱스 색칠했을 경우, 얻을 수 있는 결과 단순 저장 배열
for i in range(1, n + 1):
    if statues[i-1] == 1:
        paint[i] = paint[i-1] - 1
    else:
        paint[i] = paint[i-1] + 1
res_paint = paint[1:]
mini, maxi = min(res_paint), max(res_paint)
if mini < 0 and maxi < 0:
    print(abs(mini))
elif mini <= 0 and maxi >= 0:
    print(abs(mini - maxi))
else:
    print(abs(maxi))
