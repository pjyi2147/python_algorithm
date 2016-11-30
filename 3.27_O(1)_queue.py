#3.27 programming exercise
#import Node
import time
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next

    def setNext(self, otherNode):
        self.next = otherNode

    def getData(self):
        return self.data

class Queue:
    def __init__(self):
        self.back = None
        self.front = None

    def enqueue(self, data):
        temp = Node(data)

        if self.isEmpty():
           self.front = temp
           self.back = self.front

        else:
            self.back.setNext(temp)
            self.back = self.back.getNext()

    def dequeue(self):
        if not self.isEmpty():
            front = self.front.getData()
            self.front = self.front.getNext()
            return front

        else: return "There's no item in this list"

    def isEmpty(self):
        return self.front == None


q = Queue()

t1 = time.time()
for i in range(1000000):
    q.enqueue(i)
t2 = time.time()
print("Enqueue finished!")
t3 = time.time()
for i in range(1000000):
    q.dequeue()
t4 = time.time()

print("Enqueue: %.7f, Dequeue: %.7f" % (t2 - t1, t4 - t3))
