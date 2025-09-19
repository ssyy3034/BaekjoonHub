tree = {}

n = int(input())  # 노드 개수
for _ in range(n):
    parent, left, right = input().split()
    # '.' 은 None으로 바꿔줌
    tree[parent] = (None if left == '.' else left,
                    None if right == '.' else right)

def preorder(node):
    if node is None:
        return
    print(node, end='')
    preorder(tree[node][0])  # 왼쪽 자식
    preorder(tree[node][1])  # 오른쪽 자식

def inorder(node):
    if node is None:
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])
def postorder(node):
    if node is None:
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')
preorder('A')
print("")
inorder('A')
print("")
postorder('A')
print("")