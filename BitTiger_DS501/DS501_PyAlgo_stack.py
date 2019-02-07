class Stack():
    def __init__(self):
        self.items = []

    def push(self, v):
        self.items.append(v)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peak(self):
        if self.isEmpty():
            return None
 
        return self.items[-1]

s = Stack()
s.push(1)
s.push(2)
s.push(3)

print(s.pop())
print(s.pop())
print(s.pop())
