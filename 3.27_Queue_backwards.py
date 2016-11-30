#3.27 programming exercise #5
import time
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
q = Queue()
t1 = time.time()
for i in range(200000):
    q.enqueue(i)
t2 = time.time()
print("Enqueue finished!")
t3 = time.time()
for i in range(200000):
    q.dequeue()
t4 = time.time()

t5 = t2-t1
t6 = t4-t3

print("Enqueue: %.7f, Dequeue: %.7f" % (t5, t6))
