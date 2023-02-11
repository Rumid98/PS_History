N, m, M, T, R = map(int, input().split())
# N : 운동 시간
# m : 초기 맥박
# M : 최대 맥박
# T : 1회 운동 시 증가하는 맥박
# R : 1회 휴식 시 감소하는 맥박

pulse = m  # 초기 맥박
exer = 0
time = 0
if m + T > M:
    print('-1')
else:
    while exer != N:
        if pulse + T > M:
            pulse -= R
            if pulse < m:
                pulse = m
        else:
            pulse += T
            exer += 1
        time += 1
    print(time)
