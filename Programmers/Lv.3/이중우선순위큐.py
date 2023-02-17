import heapq


def solution(operations):
    answer = [0, 0]
    queue = []
    for i in range(len(operations)):
        if operations[i][0] == 'I':
            heapq.heappush(queue, int(operations[i][2:]))
        elif operations[i][0] == 'D' and queue:
            if operations[i][2] == '1':
                queue.sort()
                queue.pop()
            else:
                heapq.heappop(queue)
    if queue:
        answer[0], answer[1] = max(queue), min(queue)

    return answer
