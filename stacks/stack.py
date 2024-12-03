class Stack:
    def __init__(self):
        self.stack = []
    
    # function for pushing value in stack
    def push(self, data):
        self.stack.append(data)
    
    # function to pop value from the stack
    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("Trying to get value from empty stack")
        data = self.stack.pop()
        return data
    
    # function to print the stack
    def print_stack(self):
        print("The stack is: {}".format(self.stack))
    
    def lenth(self):
        print("Total length of stack is: {}".format(len(self.stack)))

    # search value in stack
    def search(self, value):
        if len(self.stack) == 0:
            raise IndexError("Trying to search value on empty stacks!")
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == value:
                return len(self.stack) - 1 - i
        print("Not found")
    
    # diplay the stack on top of each other LIFO style
    def display(self):
        if len(self.stack) == 0:
            raise IndexError("Nothing to display, stack is empty!")
        print("The stack is: ")
        for i in range(len(self.stack) - 1, -1, -1):
            print(self.stack[i])

if __name__ == '__main__':
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.print_stack()
    s.display()
    s.push(50)
    s.display()
    s.pop()
    print(s.pop())
    s.display()
    s.lenth()
    print(s.search(20))
    s.push(40)
    s.push(50)
    s.push(60)
    s.push(70)
    s.display()
    print(s.search(60))