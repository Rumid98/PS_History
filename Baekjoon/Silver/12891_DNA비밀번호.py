import sys
input = sys.stdin.readline
s, p = map(int, input().split())
dna = input().strip()
acgt = list(map(int, input().split()))  # 염기의 순서 : ['A','C','G','T']
answer = 0


def minus(a):
    if a == 'A':
        acgt[0] -= 1
    elif a == 'C':
        acgt[1] -= 1
    elif a == 'G':
        acgt[2] -= 1
    else:
        acgt[3] -= 1


def plus(a):
    if a == 'A':
        acgt[0] += 1
    elif a == 'C':
        acgt[1] += 1
    elif a == 'G':
        acgt[2] += 1
    else:
        acgt[3] += 1


for i in range(p):
    minus(dna[i])
if acgt[0] <= 0 and acgt[1] <= 0 and acgt[2] <= 0 and acgt[3] <= 0:
    answer += 1
for i in range(p, s):
    minus(dna[i])
    plus(dna[i-p])
    if acgt[0] <= 0 and acgt[1] <= 0 and acgt[2] <= 0 and acgt[3] <= 0:
        answer += 1
sys.stdout.write(str(answer))
