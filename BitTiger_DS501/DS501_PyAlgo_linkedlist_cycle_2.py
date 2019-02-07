class Solution(object):
    def detectCycle(self, head):
        slow, fast = head, head
        while True:
            if fast == None or fast.next == None:
                return None

            fast, slow = fast.next.next, slow.next

            if slow == fast:
                break

        meet = fast
        while head != meet:
            head = head.next
            meet = meet.next
        return meet
