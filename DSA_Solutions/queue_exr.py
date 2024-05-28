import threading
import time
from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

q = Queue()


def place_order(orders):
        for i in orders:
            q.enqueue(i)
            print('You just received an order for %s' %i)
            time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while True:
        try:
            order_to_serve = q.dequeue()
            print('Now serving:', order_to_serve)
            time.sleep(2)
        except(IndexError):
            print("You don't have any more orders to fulfil")
            break



if __name__=='__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    thread1 = threading.Thread(target=place_order,args=(orders,))
    thread2 = threading.Thread(target=serve_order)

    thread1.start()
    thread2.start()
