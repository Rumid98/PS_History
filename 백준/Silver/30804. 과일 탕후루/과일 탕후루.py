import sys
def input(): return sys.stdin.readline().strip()


def main():
    n = int(input())
    tang = list(map(int, input().split()))
    if n == 1:
        print(1)
    else:
        fruits = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        lt, rt = 0, 1
        answer = 0
        fruits[tang[0]] += 1
        fruits[tang[1]] += 1
        while lt < rt:
            count = 0
            for i in range(1, 10):
                if fruits[i]:
                    count += 1
            if count > 2:
                fruits[tang[lt]] -= 1
                lt += 1
            else:
                answer = max(answer, rt-lt+1)
                rt += 1
                if rt == n:
                    break
                fruits[tang[rt]] += 1
        print(answer)


if __name__ == "__main__":
    main()
