class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')

F.left = B
F.right = G
B.left = A
B.right = D
D.left = C
D.right = E
G.right = I
I.left = H

from DS501_PyAlgo_stack import Stack
from DS501_PyAlgo_queue import Queue

def dfs_recursion(root):
    def traverse(node):
        if not node:
            return

        print(node.val, end='')
        traverse(node.left)
        traverse(node.right)

    traverse(root)

def dfs_loop(root):
    stack = Stack()
    stack.push(root)

    while not stack.isEmpty():
        node = stack.pop()
        print(node.val, end='')

        if node.right:
            stack.push(node.right)
        if node.left:
            stack.push(node.left)

print("="*20)
dfs_recursion(F)
print('')
dfs_loop(F)
print('')

def bfs_loop(root):
    queue = Queue()
    queue.enqueue(root)

    while not queue.isEmpty():
        node = queue.dequeue()
        print(node.val, end='')

        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

print('='*20)
bfs_loop(F)
print('')
