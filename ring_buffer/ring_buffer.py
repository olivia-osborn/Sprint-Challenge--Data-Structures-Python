class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # set value at index self.current to item value
        self.storage[self.current] = item
        # if self.current is at max capacity
        if self.current == (self.capacity - 1):
            # set self.current to 0
            self.current = 0
        # else, set self.current to next index
        else:
            self.current += 1

    def get(self):
        arr = []
        for i in self.storage:
            if i != None:
                arr.append(i)
        return arr


ring = RingBuffer(5)
print(len(ring.storage))  # 5)

ring.append('a')
ring.append('b')
ring.append('c')
ring.append('d')
print(len(ring.storage))  # 5
print(ring.get())  # ['a', 'b', 'c', 'd']

ring.append('e')
print(len(ring.storage))  # , 5)
print(ring.get())  # , ['a', 'b', 'c', 'd', 'e'])

ring.append('f')
print(len(ring.storage))  # , 5)
print(ring.get())  # , ['f', 'b', 'c', 'd', 'e'])

ring.append('g')
ring.append('h')
ring.append('i')
print(len(ring.storage))  # , 5)
print(ring.get())  # , ['f', 'g', 'h', 'i', 'e'])
