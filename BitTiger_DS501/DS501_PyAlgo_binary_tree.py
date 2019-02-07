class Node():
    def __init__(self, val):
        self.left = None # left child
        self.right = None # right child
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
