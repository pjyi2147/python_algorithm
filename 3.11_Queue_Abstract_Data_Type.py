#3.11 Queue Abstract Data Type
import time 
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
t1 = time.time()
for i in range(100000):
    q.enqueue(i)
t2 = time.time()

t3 = time.time()
for i in range(100000):
    q.dequeue()
t4 = time.time()

t5 = t2-t1
t6 = t4-t3

print("Enqueue: %.7f, Dequeue: %.7f" % (t5, t6))
