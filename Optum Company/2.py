'''
2. Implement queue using two stacks.
'''

class Stack:
    def __init__(self):
        self.items = []

    def get_size(self):
        return len(self.items)
    
    def is_empty(self):
        return self.get_size()==0

    def push(self,val):
        self.items.append(val)        

    def pop(self):
        return self.items.pop()


class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()
    
    def insert(self,val):
        self.s1.push(val)
    
    def remove(self):
        if self.is_empty():
        	print("Queue Underflow")
        	return

        
        while self.s1.get_size()>1:
            self.s2.push(self.s1.pop())
        x = self.s1.pop()
        
        while not self.s2.is_empty():
        	self.s1.push(self.s1.pop())

        return x    

