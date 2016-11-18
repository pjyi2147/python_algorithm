from pythonds.basic.queue import Queue

def hotPotato(lst, num):
    simqueue = Queue()
    for name in lst:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPotato(['a','b','c','d','e','f'] , 7))

