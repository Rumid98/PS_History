t = int(input())  # 테스트 케이스 개수
# command -> R: 뒤집기, D: 버리기 (첫 번째 수)
for i in range(t):
    answer = ''
    command = input().strip()  # 수행할 함수
    n = int(input())
    input_line = input().strip()
    arr = []
    if len(input_line) > 2:  # 빈 배열이 아닌 경우
        tmp = list(map(int, input_line[1:-1].split(',')))
        arr = [str(x) for x in tmp]

    # 초기 상태: 첫 번째 수를 버림, '뒤집기'를 실행하면 맨 마지막 수를 버림
    state = True  # state가 True면 첫 번째 수 버리기, False면 맨 마지막 수를 버림
    end = True  # 종료 조건: 빈 배열에서 D 명령 실행
    # command 탐색
    for c in command:
        if c == 'R':
            state = True if not state else False  # 상태 변경
        elif c == 'D':
            if state:  # 첫 번째 수 버리는 경우
                if arr:
                    del arr[0]
                else:
                    end = False
                    break
            else:  # 맨 마지막 수 버리는 경우
                if arr:
                    del arr[-1]
                else:
                    end = False
                    break
    if end:  # 정상적 종료
        answer = '['
        if state:  # 앞에서 부터
            answer += ','.join(arr)
        else:
            answer += ','.join(reversed(arr))
        answer += ']'
    else:
        answer = 'error'
    print(answer)
