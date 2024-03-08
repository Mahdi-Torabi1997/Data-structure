class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("dequeue from empty queue")

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
