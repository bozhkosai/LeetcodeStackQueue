"""queue"""

class Node:
    """node"""
    def __init__(self, data=0):
        self.data = data
        self.next = None

class Queue:
    """queue"""
    def __init__(self, head = None, length = 0):
        self.head = head
        self.length = length

    def push(self, x: int) -> None:
        """push"""
        node = Node(x)
        if self.head:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        else:
            self.head = node
        self.length += 1

    def pop(self) -> int:
        """pop"""
        if self.head:
            data, self.head = self.head.data, self.head.next
            self.length -= 1
            return data

    def peek(self) -> int:
        """peek"""
        return self.head.data

    def len(self) -> int:
        """len"""
        return self.length

    def empty(self) -> bool:
        """empty"""
        return not self.head

class MyStack:
    """my stack"""
    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        """push"""
        self.queue.push(x)
        for _ in range(self.queue.len() - 1):
            self.queue.push(self.queue.pop())

    def pop(self) -> int:
        """pop"""
        return self.queue.pop()

    def top(self) -> int:
        """top"""
        return self.queue.peek()

    def empty(self) -> bool:
        """empty"""
        return self.queue.empty()
