import sys
input = sys.stdin.readline


# n, m은 1~100,000 -> list로 O(n^2) -> 무조건 시간초과
# 찾아보니 딕셔너리는 탐색 시간이 O(1)
pokemon_1 = {}  # {숫자: 단어} 구성
pokemon_2 = {}  # {단어: 숫자} 구성
n, m = map(int, input().split())
for i in range(1, n+1):
    poke = input().strip()
    pokemon_1[i] = poke
    pokemon_2[poke] = i
for _ in range(m):
    command = input().strip()
    if command.isdigit():
        sys.stdout.write(pokemon_1[int(command)] + '\n')
    else:
        sys.stdout.write(str(pokemon_2[command]) + '\n')
