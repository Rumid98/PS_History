from collections import deque


def solution(a, b, documents):
    queue = deque()
    priority = [0 for _ in range(10)]  # 중요도 개수 파악 배열
    for i in range(len(documents)):
        priority[documents[i]] += 1
        queue.append((i, documents[i]))  # queue에 (문서 index, 문서 중요도) 형태로 삽입

    max_priority = 0  # 현재 존재하는 가장 높은 중요도 저장 변수
    for i in range(10):
        if priority[i]:
            max_priority = i
    count = 0
    while queue and max_priority > 0:
        tmp = queue.popleft()
        if tmp[1] == max_priority:  # 가장 높은 중요도인 경우
            count += 1  # 출력은 확정이므로 count +1
            priority[max_priority] -= 1  # 해당 중요도 개수 -1
            if tmp[0] == b:  # 문제에서 구하고자하는 index 문서
                return count  # 출력 순서 반환
            if not priority[max_priority]:  # 해당 중요도의 문서가 더 이상 없다면
                for j in range(max_priority, 0, -1):  # 현재 중요도부터 내림차순으로
                    if priority[j]:  # 해당 중요도 문서가 있다면
                        max_priority = j  # 바꿔줌
                        break
        else:
            queue.append(tmp)


t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    n, m = map(int, input().split())  # 문서 개수, n번째 index 문서 출력 순서 구하기
    documents = list(map(int, input().split()))  # 문서 배열
    print(solution(n, m, documents))
