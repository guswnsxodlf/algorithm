# Created by Jello on 2017. 6. 29.


class Graph:
    def __init__(self, v):
        self.matrix = [[0]*v for x in range(v)]

    def set(self, v1, v2, flag):
        self.matrix[v1-1][v2-1] = flag
        self.matrix[v2-1][v1-1] = flag

    def is_connect(self, v1, v2):
        if self.matrix[v1-1][v2-1] == 1:
            return True
        else:
            return False

# When
g = Graph(10)
g.set(1, 8, 1)
g.set(1, 9, 1)
g.set(2, 8, 1)
g.set(2, 3, 1)
g.set(3, 6, 1)
g.set(3, 9, 1)

# Then
assert g.is_connect(1, 8)
assert not g.is_connect(5, 10)
