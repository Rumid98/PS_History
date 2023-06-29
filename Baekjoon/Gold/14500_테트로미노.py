n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
tetro = [[[0, 1], [0, 1], [0, 1]], [[1, 0], [1, 0], [1, 0]],                                                            # 2개
         [[0, 1], [1, 0], [0, -1]],                                                                                     # 1개
         [[1, 0], [1, 0], [0, 1]], [[0, 1], [0, 1], [-1, 0]], [[-1, 0], [-1, 0], [0, -1]], [[-1, 0], [0, 1], [0, 1]],   # 4개
         [[1, 0], [1, 0], [0, -1]], [[0, 1], [0, 1], [1, 0]], [[-1, 0], [-1, 0], [0, 1]], [[0, -1], [0, -1], [-1, 0]],  # 4개
         [[1, 0], [0, 1], [1, 0]], [[0, 1], [-1, 0], [0, 1]],                                                           # 2개
         [[1, 0], [0, -1], [1, 0]], [[0, 1], [1, 0], [0, 1]],                                                           # 2개
         [[0, 1], [0, 1], [1, -1]], [[1, 0], [1, 0], [-1, 1]], [[0, 1], [0, 1], [-1, -1]], [[1, 0], [1, 0], [-1, -1]]]  # 4개
answer = 0


for i in range(n):  # graph 행 개수
    for j in range(m):  # graph 열 개수
        for k in range(len(tetro)):  # 테트로미노 개수 (총 5개)
            x, y = i, j  # 시작 좌표
            tmp = graph[i][j]
            for l in range(3):  # 각 테트로미노 별 이동 횟수
                x += tetro[k][l][0]
                y += tetro[k][l][1]
                if 0<=x<n and 0<=y<m:  # 테트로미노가 graph 안에 위치
                    tmp += graph[x][y]
                else:  # 그렇지 않으면 break
                    break
            else:  # 블럭 모두 graph 안에 위치했을 경우만 count
                #print(f'index: ({i}, {j}) + tetromino 번호: {k+1}  ->  value: {tmp}')
                answer = max(answer, tmp)
print(answer)
