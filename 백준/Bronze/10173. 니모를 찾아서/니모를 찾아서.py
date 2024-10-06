import sys
input = sys.stdin.readline


def main():
    while True:
        line = input().strip()
        if line == 'EOI':
            break
        if 'nemo' in line.lower():
            print('Found')
        else:
            print('Missing')


if __name__ == "__main__":
    main()
