class Queue():
    def __init__(self):
        self.items =[]

    def enqueue(self, v):
        self.items.append(v)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def peak():
        if self.isEmpty():
            return None
        return self.items[0]

