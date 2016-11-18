#3.16 deque abstract data type
class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.items)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()


d = Deque()
print(d.isEmpty())
d.addRear(4)		 
d.addRear('dog')
d.addFront('cat')		 
d.addFront(True)		 
print(d.size())
print(d.isEmpty())
print(d.addRear(8.4))
print(d.removeRear())
print(d.removeFront())


