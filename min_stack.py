class MinStack:

# get minimum element in stack in constant time O(1)
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.myStack = []
        self.miniStack=[]
        
    def push(self, x: int) -> None:
        if(len(self.myStack) == 0):
            self.miniStack.append(x)
        else:
            self.miniStack.append(min(self.miniStack[-1],x))
        self.myStack.append(x)

    def pop(self) -> None:
        if(len(self.myStack) != 0):
            self.miniStack.pop()
            self.myStack.pop()

    def top(self) -> int:
        return self.myStack[-1]
        
    def getMin(self) -> int:
        return self.miniStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()