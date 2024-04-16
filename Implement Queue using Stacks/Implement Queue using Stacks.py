"""queue"""

class Node:
    """node"""
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """stack"""
    def __init__(self, top = None):
        self.top = top

    def push(self, x: int) -> None:
        """push"""
        node = Node(x)
        node.next = self.top
        self.top = node

    def pop(self) -> int:
        """pop"""
        if not self.empty():
            data = self.top.data
            self.top = self.top.next
            return data

    def peek(self) -> int:
        """peek"""
        if not self.empty():
            return self.top.data

    def empty(self) -> bool:
        """empty"""
        return self.top is None

class MyQueue:
    """queue"""
    def __init__(self):
        self.stack = Stack()

    def push(self, x: int) -> None:
        """push"""
        stack_ = Stack()
        while not self.stack.empty():
            stack_.push(self.stack.pop())
        self.stack.push(x)
        while not stack_.empty():
            self.stack.push(stack_.pop())

    def pop(self) -> int:
        """pop"""
        return self.stack.pop()

    def peek(self) -> int:
        """peek"""
        return self.stack.peek()

    def empty(self) -> bool:
        """empty"""
        return self.stack.empty()