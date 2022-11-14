class Stack():

    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        # or self.items.insert(0, item)
    
    def pop(self):
        if len(self.items) == 0:
            print("Warning - Stack is empty")
            return
        return self.items.pop()
        # or self.items.pop(0)
    
    def peek(self):
        return self.items[len(self.items) - 1]
        # or self.items[0]
    
    def size(self):
        return len(self.items)