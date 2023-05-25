cards = [0 for _ in range(20_000_001)]
n = int(input())
tmp = list(map(int, input().split()))
for x in tmp:
    cards[x + 10_000_000] += 1
m = int(input())
check = list(map(int, input().split()))
answer = []
for c in check:
    if cards[c + 10_000_000]:
        answer.append('1')
    else:
        answer.append('0')
print(' '.join(answer))
