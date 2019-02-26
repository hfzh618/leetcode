class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.insert(0, x)
        print('q1', self.queue1)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        print('len', len(self.queue1))
        for _ in range(len(self.queue1)-1):
            self.queue2.insert(0, self.queue1.pop())
        print(self.queue1)
        res = self.queue1.pop()
        self.queue1 = self.queue2
        self.queue2 = []
        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        self.queue2 = self.queue1[:]
        for _ in range(len(self.queue1)-1):
            self.queue1.pop()
        res = self.queue1[-1]
        self.queue1 = self.queue2
        self.queue2 = []
        return res

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue1):
            return False
        return True


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
print(obj.top())
obj.pop()
obj.pop()
print(obj.empty())

# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# print(q.empty())