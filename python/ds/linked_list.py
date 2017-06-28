# Created by Jello on 2017. 6. 29.


class Node:
    def __init__(self, e, nxt=None):
        self.next = nxt
        self.data = e


class LinkedList:
    def __init__(self):
        self.head = Node(None)

    def insert(self, node, e):
        new_node = Node(e)
        if node.next != None:
            new_node.next = node.next
        node.next = new_node
        return new_node

    def search(self, e):
        node = self.head
        while node.next != None:
            if node.next.data == e:
                return node
            node = node.next

        return None

    def print_all(self):
        node = self.head
        while node.next != None:
            print(node.next.data, end=' ')
            node = node.next
        print()

    def delete(self, node):
        if node.next != None:
            remove_node = node.next
            if remove_node.next != None:
                node.next = remove_node.next
            else:
                node.next = None


l = LinkedList()

a = l.insert(l.head, 3)
l.insert(a, 6)

l.print_all()   # 3 6

l.delete(a)

l.print_all()   # 3
