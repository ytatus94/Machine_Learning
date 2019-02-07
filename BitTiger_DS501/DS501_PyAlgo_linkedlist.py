class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Doubly_linked_list():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data, None, None)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            node.next = None
            self.tail.next = node
            self.tail = node

    def remove(self, value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.head:
                    self.head = curr.next
                else:
                    # A->curr->B, A->B
                    curr.prev.next = curr.next
                if curr == self.tail:
                    self.tail = curr.prev
                else:
                    # A->curr->B, B.prev->A
                    curr.next.prev = curr.prev
            curr = curr.next

    def print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
        print('**********')

    def hasCycle(self):
        fast, slow = self.head, self.head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        return False

d = Doubly_linked_list()

#d.append(1)
#d.append(2)
#d.append(3)
#d.append(4)
#d.print()
#d.remove(1)
#d.remove(3)
#d.print()
#d.remove(2)
#d.remove(4)
#d.print()
#d.remove(6)
#d.print()

d.append(1)
d.append(2)
d.append(3)
d.append(4)
#n4 = d.tail
d.append(5)
d.append(6)
d.append(7)
d.append(8)
#d.tail.next = n4

#d.print()
print(d.hasCycle())
