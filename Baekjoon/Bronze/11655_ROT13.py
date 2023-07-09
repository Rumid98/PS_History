str = input()
answer = ''
for c in str:
    if 'a' <= c <= 'z':  # 소문자 case
        answer += chr(ord(c) + 13) if ord(c) + 13 <= ord('z') else chr(ord('a') + ord(c) + 12 - ord('z'))
    elif 'A' <= c <= 'Z':  # 대문자 case
        answer += chr(ord(c) + 13) if ord(c) + 13 <= ord('Z') else chr(ord('A') + ord(c) + 12 - ord('Z'))
    else:  # 나머지 case
        answer += c
print(answer)
