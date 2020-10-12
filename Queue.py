"""Queue Implementation for Graph Algorithms"""


class Queue():

    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, element):
        self.queue.insert(0, element)
        self.size += 1

    def peek(self):
        return self.queue[len(self.queue)-1]

    def dequeue(self):
        result = self.queue[len(self.queue)-1]
        self.queue.pop()
        return result
        self.size -= 1

    def is_empty(self):
        return self.queue == []
