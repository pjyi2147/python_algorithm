#3.21 The unordered list class
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def append(self, item):
        current = self.head
        temp = Node(item)
        if self.head == None:
            temp.setNext(current)
            self.head = temp

        else:
            while current.getNext() != None:
                current = current.getNext()

            temp.setNext(current.getNext())
            current.setNext(temp)

    def insert(self, location, item):
        temp = Node(item)
        current = self.head
        previous = None
        count = 0
        while count < location:
            previous = current
            current = current.getNext()
            count = count + 1

        temp.setNext(current)
        previous.setNext(temp)
        

    def index(self, item):
        current = self.head
        found = False
        count = 0
        while (not found) and count < self.size():
            if current.getData() == item:
                return count

            else:
                count = count + 1
                current = current.getNext()

        return "No item in this list"

    def pop(self, index=0):                     #index=0  기본값 설정
        current = self.head
        previous = None 
        count = 0
        if index == 0:
            self.head = current.getNext()
            return current.getData()
            
        while count < index:
            count = count + 1
            previous = current
            current = current.getNext()
            
        previous.setNext(current.getNext())
        return current.getData()
         
    
mylist = UnorderedList()

mylist.append(0)
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append(5)



print(mylist.pop())
print(mylist.size())
print(mylist.index(309))

"""
print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())

mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))
"""
