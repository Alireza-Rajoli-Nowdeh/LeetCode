#This code is about OOP and class and encapsulation / I can learn using Class/ methods and .... 

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.count = 0

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.count = len(self.stack1)
        if len(self.stack2) == 0:
            while self.count >0:
                top=self.stack1.pop()
                self.stack2.append(top)
                self.count = self.count -1
            pop = self.stack2.pop()
            return pop
        return self.stack2.pop()

    def peek(self) -> int:
        self.count = len(self.stack1)
        if len(self.stack2) == 0:
            while self.count >0:
                top=self.stack1.pop()
                self.stack2.append(top)
                self.count = self.count -1
            peek = self.stack2.pop()
            self.stack2.append(peek)
            return peek
        peek2= self.stack2.pop()
        self.stack2.append(peek2)
        return peek2

    def empty(self) -> bool:
        if len(self.stack2) ==0 and len(self.stack1) ==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
