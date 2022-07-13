import argparse
from collections import deque
from threading import Thread, current_thread
from time import sleep
from colorama import Fore


class Queue:
    def __init__(self, initialList = []):
        """FIFO - Constructor"""
        self.container = deque(initialList)

    def __str__(self):
        finalPrint = " ".join(str(i) for i in self.container)
        return finalPrint

    def isEmpty(self):
        """Checks whether the queue is empty or not."""
        return self.size() <= 0

    def enque(self, value):
        """Adds the element to the queue."""
        self.container.appendleft(value)
        # self.container.insert(0, value)
        return f'{value} inserted!'

    def deque(self):
        """Removes the element from the queue."""
        if self.isEmpty():
            return 'Queue is empty.'
        ele = self.container.pop()
        return ele
        # return f'{ele} popped out!'

    def front(self):
        """To see the first element at the front end of the queue"""
        if self.isEmpty():
            return 'Queue is empty.'
        return self.container[-1]
        # return f'{self.container[-1]} is the front of the queue.'

    def size(self):
        """Return the size of the queue."""
        return len(self.container)
        # return f'The size of the queue is {len(self.container)}'

def placeOrder(order, queueObject):
    for i in range(len(order)):
        _ = queueObject.enque(order[i])
        print(Fore.YELLOW + f'{current_thread().getName()}: Order Placed - {order[i]}')
        sleep(0.5)

def serveOrder(order, queueObject):
    for i in range(len(order)):
        servedOrder = queueObject.deque()
        print(Fore.GREEN + f'{current_thread().getName()}: Order Served - {servedOrder}')
        sleep(2)

if __name__ == "__main__":
    queue = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = Thread(target = placeOrder, args = (orders, queue))
    t2 = Thread(target = serveOrder, args = (orders, queue))

    t1.start()
    sleep(1)
    t2.start()

    t1.join()
    t2.join()

    print(Fore.WHITE + "BYE = ",current_thread().getName())
