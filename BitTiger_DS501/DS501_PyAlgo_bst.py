class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node):
        def _insert(curr):
            if node.val <= curr.val:
                if curr.left:
                    _insert(curr.left)
                else:
                    curr.left = node
            elif node.val > curr.val:
                if curr.right:
                    _insert(curr.right)
                else:
                    curr.right = node

        if self.root is None:
            self.root = node
        else:
            _insert(self.root)

    def sort(self):
        def inorder(curr):
            if curr:
                inorder(curr.left)
                print(curr.val)
                inorder(curr.right)
        inorder(self.root)

    def has(self, val):
        def _find(curr):
            if curr is None:
                return False
            elif val == curr.val:
                return True
            elif val < curr.val:
                return _find(curr.left)
            else:
                return _find(curr.right)
        return _find(self.root)

    def delete(self, val):
        def findMin(node):
            curr = node
            while curr.left is not None:
                curr = curr.left
            return curr

        def _delete(curr, target):
            if curr is None:
                return curr
            if target < curr.val:
                curr.left = _delete(curr.left, target)
            elif target > curr.val:
                curr.right = _delete(curr.right, target)
            else:
                if curr.left is None:
                    temp = curr.right
                    curr = None
                    return temp
                elif curr.right is None:
                    temp = curr.left
                    curr = None
                    return temp

                temp = findMin(curr.right)
                curr.val = temp.val
                curr.right = _delete(curr.right, temp.val)
            return curr

        self.root = _delete(self.root, val)

bst = BST()
bst.insert(Node(6))
bst.insert(Node(8))
bst.insert(Node(5))
bst.insert(Node(4))
bst.insert(Node(7))
bst.insert(Node(2))
bst.insert(Node(3))

bst.sort()

print("="*20)
print(bst.has(2))
print(bst.has(3))
print(bst.has(4))
print(bst.has(5))
print(bst.has(6))
print(bst.has(7))
print(bst.has(8))
print(bst.has(9))
print(bst.has(0))

print("="*20)
bst.delete(6)
bst.delete(2)
bst.delete(4)
bst.delete(8)
bst.sort()

print("="*20)
bst.delete(7)
bst.delete(5)
bst.delete(3)
bst.sort()

print("="*20)
print(bst.root.val)
print(bst.root.left.val)
print(bst.root.right.val)
