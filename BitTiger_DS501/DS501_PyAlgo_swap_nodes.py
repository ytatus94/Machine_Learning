class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        root = ListNode(0)
        root.next = head

        curr = root

        while curr.next and curr.next.next:
            p1 = curr.next
            p2 = curr.next.next

            # curr->p1->p2
            curr.next = p2
            p1.next = p2.next
            p2.next = p1

            curr = curr.next.next
        return root.next
