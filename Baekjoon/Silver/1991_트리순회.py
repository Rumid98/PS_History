n = int(input())
trees = {}
for _ in range(n):
    root, left, right = input().split()
    trees[root] = [left, right]


def preorder(v):  # 전위
    if v == '.':
        return
    print(v, end='')
    preorder(trees[v][0])
    preorder(trees[v][1])


def inorder(v):  # 중위
    if v == '.':
        return
    inorder(trees[v][0])
    print(v, end='')
    inorder(trees[v][1])


def postorder(v):  # 후위
    if v == '.':
        return
    postorder(trees[v][0])
    postorder(trees[v][1])
    print(v, end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')
