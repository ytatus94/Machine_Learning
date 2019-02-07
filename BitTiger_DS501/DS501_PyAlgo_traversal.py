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

def preorder(root):
    def traverse(node):
        if not node:
            return

        print(node.val)
        traverse(node.left)
        traverse(node.right)

    traverse(root)

def postorder(root):
    def traverse(node):
        if not node:
            return

        traverse(node.left)
        traverse(node.right)
        print(node.val)

    traverse(root)
 
def inorder(root):
    def traverse(node):
        if not node:
            return

        traverse(node.left)
        print(node.val)
        traverse(node.right)

    traverse(root) 

preorder(F)
print("="*20)
postorder(F)
print("="*20)
inorder(F)
