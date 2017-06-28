# Created by Jello on 2017. 6. 29.


class Graph:
    def __init__(self, v):
        self.list = [set() for x in range(v)]

    def connect(self, v1, v2):
        self.list[v1-1].add(v2)
        self.list[v2-1].add(v1)

    def disconnect(self, v1, v2):
        self.list[v1-1].remove(v2)
        self.list[v2-1].remove(v1)

    def is_connect(self, v1, v2):
        if v2 in self.list[v1-1]:
            return True
        else:
            return False

# When
g = Graph(10)
g.connect(1, 8)
g.connect(1, 9)
g.connect(2, 8)
g.connect(2, 3)
g.connect(3, 6)
g.connect(3, 9)
g.disconnect(2, 3)
g.disconnect(3, 6)

# Then
assert g.is_connect(1, 8)
assert g.is_connect(1, 9)
assert not g.is_connect(2, 3)
assert not g.is_connect(3, 6)
assert not g.is_connect(1, 2)
