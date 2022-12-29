import sys
input = sys.stdin.readline
n = int(input())
text = input().strip()


s_count, b_count = 0, 0
for x in text:
    if x == 's':
        s_count += 1
    elif x == 'b':
        b_count += 1
if s_count == b_count:
    sys.stdout.write("bigdata? security!\n")
elif s_count > b_count:
    sys.stdout.write("security!\n")
else:
    sys.stdout.write("bigdata?\n")
