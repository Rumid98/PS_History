def solution(s):
    answer = True
    queue = []
    if s[0] == ')':  # 처음 시작이 ')'인 경우
        answer = False
    else:  # 처음 시작이 '('인 경우
        for i in s:
            if i == '(':  # 왼괄호면 상관없이 append
                queue.append(i)
            elif i == ')' and queue:  # 오른괄호, 닫힐 괄호가 있는 경우
                queue.pop()
            elif i == ')' and not queue:  # 오른괄호, queue가 비었을 경우
                answer = False
                break
        if queue:  # 탐색이 끝났는데 queue에 아직 왼괄호가 남은 경우
            answer = False
    return answer