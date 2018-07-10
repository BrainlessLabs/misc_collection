from threading import *
import threading
import time
import random
from pprint import pprint as println

# The queue to be used for consumers
"""
This is a single first in and first out queue.
This puts the item in the end of queue an gets the first item
"""


class OwnQueue(object):
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue):
            return self.queue.pop(0)
        else:
            raise ValueError('No Elements')

    def peek(self):
        if len(self.queue):
            return self[0]
        else:
            raise ValueError('No Elements')

    def __len__(self)->int:
        return len(self.queue)


class Producer(Thread):
    def __init__(self, thread_id: int, thread_name: str, modify_event: Event, queue:OwnQueue):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.modify_event = modify_event
        self.queue = queue
        println(self.__repr__())

    def run(self):
        while True:
            # Choose how many elements we want to insert at one shot
            number_of_elements_to_insert = random.choice([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
            # Let others know that we are modifying the queue
            self.modify_event.set()
            for i in range(number_of_elements_to_insert):
                val = random.randint(i, 100001)
                self.queue.push(val)
            println('%s Produced %d elements' % (self.__repr__(), number_of_elements_to_insert))
            # Let others know that modification is done and the queue is ready
            self.modify_event.clear()

    def __repr__(self):
        return 'Producer Thread Name: {}, Thread Id: {}'.format(self.thread_name, self.thread_id)


class Consumer(Thread):
    """
    Consumers are of 2 types:
    1. Pop Consumers that pop the last element and modify the queue
    2. Peek Consumers that peek the last element and do not modify the queue
    """
    def __init__(self, thread_id: int, thread_name: str, modify_event: Event, queue:OwnQueue):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.modify_event = modify_event
        self.queue = queue
        # This choice flag at random determines if the consumer is a pop or a peek consumer
        self.pop_consumer = random.choice([True, False])
        println(self.__repr__())

    def run(self):
        while not self.modify_event.isSet():
            # I have to set it here so that no one modifies the queue while we are checking len
            self.modify_event.set()
            if not len(self.queue):
                self.modify_event.wait()
            else:
                if self.pop_consumer is True:
                    println('{} Popped Element {}'.format(self.__repr__(), self.queue.pop()))
                else:
                    println('{} Peeked Element {}'.format(self.__repr__(), self.queue.peek()))

            self.modify_event.clear()

    def __repr__(self):
        pop_str = 'Peek'
        if self.pop_consumer is True:
            pop_str = 'Pop '
        return '{} Consumer Thread Name: {}, Thread Id: {}'.format(pop_str, self.thread_name, self.thread_id)


"""
@details: The main program that gets called. The starting point for the program.
"""
if __name__ == "__main__":
    modify_event = Event()

    producer_threads = []
    consumer_threads = []
    number_of_consumers = random.choice([10, 20, 30, 40, 50, 100])
    number_of_producers = random.choice([10, 20, 30, 40])
    queue = OwnQueue()

    for i in range(number_of_consumers):
        consumer_threads.append(Consumer(thread_id=i, thread_name='Thread_{}'.format(i), modify_event=modify_event, queue= queue))
        consumer_threads[-1].start()

    for i in range(number_of_producers):
        producer_threads.append(Producer(thread_id=i, thread_name='Thread_{}'.format(i), modify_event=modify_event, queue= queue))
        producer_threads[-1].start()
