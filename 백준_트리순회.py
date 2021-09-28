# 전위순회 루트를 방문처리후 왼쪽 자식을 처리 왼쪽자식이 존재하면 계속 처리 다시 재귀되면서 오른쪽 자식이 있으면 처리

graph = {}
n = int(input())
for i in range(n):
    root, left, right = input().split()
    graph[root] = (left, right)

preorder_list = []
def preorder(data):
    if data == '.': return
    preorder_list.append(data)
    preorder(graph[data][0])
    preorder(graph[data][1])

inorder_list = []
def inorder(data):
    if data == '.': return
    inorder(graph[data][0])
    inorder_list.append(data)
    inorder(graph[data][1])

postorder_list = []
def postorder(data):
    if data == '.': return
    postorder(graph[data][0])
    postorder(graph[data][1])
    postorder_list.append(data)


preorder('A')
print(''.join(preorder_list))
inorder('A')
print(''.join(inorder_list))
postorder('A')
print(''.join(postorder_list))
