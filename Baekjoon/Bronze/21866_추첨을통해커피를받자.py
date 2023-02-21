scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]
input_scores = list(map(int, input().split()))
answer = 'draw'
if sum(input_scores) < 100:
    answer = 'none'
for a, b in zip(scores, input_scores):
    if b > a:
        answer = 'hacker'
        break
print(answer)
