#3.11 Queue Abstract Data Type
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def size(self):
        return len(self.items)

    def dequeue(self):
        return self.items.pop()


q = Queue()
print(q.isEmpty())
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.isEmpty())
print(q.dequeue())
print(q.size())
q.enqueue('print')
print(q.dequeue())
