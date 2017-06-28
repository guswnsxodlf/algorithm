# Created by Jello on 2017. 6. 29.


class Queue:
    def __init__(self, length):
        self.data = [None] * length
        self.front = 0
        self.rear = 0

    def put(self, e):
        if self.rear > len(self.data)-1:
            if self.front == 0:
                return False
            else:
                self.shift()
        self.data[self.rear] = e
        self.rear += 1
        return e

    def get(self):
        if self.front == self.rear:
            return False

        result = self.data[self.front]
        self.front += 1
        return result

    def shift(self):
        print("shift")
        for i in range(self.front, self.rear):
            self.data[i-self.front] = self.data[i]
        self.rear -= self.front


q = Queue(5)

print(q.put(1), end=' ')
print(q.put(2), end=' ')
print(q.put(3), end=' ')
print(q.put(4), end=' ')
print(q.put(5))

print(q.get(), end=' ')   # 1
print(q.get(), end=' ')   # 2
print(q.get())   # 3

print(q.put(6), end=' ')   # shift
print(q.put(7))
