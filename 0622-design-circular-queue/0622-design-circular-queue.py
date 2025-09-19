class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.head = -1
        self.tail = -1
        self.data = [None]*k
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail+1)%self.cap
        self.data[self.tail]= value
        self.count+=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.count == 1:
            self.head = -1
            self.tail = -1
            self.count = 0
        else:
            self.head = (self.head+1) % self.cap
            self.count -=1
        return True


    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.data[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.data[self.tail]

    def isEmpty(self) -> bool:
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.count == self.cap:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()