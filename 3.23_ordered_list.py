#3.23 Implementing an Ordered List
class Node:
    def __init__(self, initdata):
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


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True

            else:
                if currnet.getData() > item:
                    stop = True
                else: current = current.getNext()

        return found

    def add(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True

            else:
                previous = current
                current = current.getNext()

        if previous == None:                    #current
            temp.setNext(self.head)
            self.head = temp

        else:
            temp.setNext(current)
            previous.setNext(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current == None:
                return ValueError("item not in list")
                break
            
            elif current.getData() == item:
                found = True
                if previous == None:
                    self.head = current.getNext()

                else: previous.setNext(current.getNext())

            else:
                previous = current
                current = current.getNext()

            

a = OrderedList()
a.add(23)
a.add(45)
a.add(35)
a.add(356)
print(a.remove(392))
print(a.size())
print(a.search(23))







            
            
