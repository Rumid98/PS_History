import sys
import heapq
input = sys.stdin.readline
alpha_check = [0] * 26
a = input().strip()
b = input().strip()


answer = 0
for x in a:
    alpha_check[ord(x)-ord('a')] += 1
for y in b:
    alpha_check[ord(y)-ord('a')] -= 1
for i in range(26):
    answer += abs(alpha_check[i])
sys.stdout.write(str(answer))
