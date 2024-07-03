import sys
def input(): return sys.stdin.readline().strip()


def main():
    word = input()
    print(ord(word) - ord('가') + 1)
    

if __name__ == "__main__":
    main()
