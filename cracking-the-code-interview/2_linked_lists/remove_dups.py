"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
"""

from queue import Empty


class LinkedList:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("List is empty")
        return self._head._element

    def last(self):
        if self.is_empty():
            raise Empty("List is empty")
        return self._tail._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("List is empty")
        ans = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return ans

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def after(self):
        pass

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            try:
                yield cursor
                cursor = self.dequeue()
            except Empty:
                break


def solve():
    pass


if __name__ == "__main__":
    l = LinkedList()
    l.enqueue(1)
    l.enqueue(2)
    l.enqueue(3)
    l.enqueue(4)
    l.enqueue(5)
    # print(len(l))
    for elem in l:
        print(elem)
