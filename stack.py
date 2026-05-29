# Using List And Array
"""stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)

# peek
peek = stack[-1]
print(peek)

# pop
pop = stack.pop()
print(pop)

# Stack after pop
print(stack)

# is Empty
isEmpty = not bool(stack)
print(isEmpty)

# size
size = len(stack)
print(size)
"""

# Using Class

class stack:
    def __init__(self):
        self.stack = []

    def add(self,element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0     

    def lenth(self):
        return len(self.stack)
    
my_stack = stack()
my_stack.add('A')
my_stack.add('B')
my_stack.add('C')
print(my_stack.stack)   
print(my_stack.pop())   
print(my_stack.peek())   
print(my_stack.isEmpty())   
print(my_stack.lenth())   
            
# Using Linked List
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,value):
        new_node = Node(value)   
        new_node.next = self.head
        self.head = new_node
        self.size += 1    

    def pop(self):
        if self.head is None:
            return "Stack is Empty"
        popNode = self.head
        self.head = self.head.next
        self.size -= 1
        return popNode.value
    
    def peek(self):
        return self.head.value
    
    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size()      

   


my_stack = Stack()
my_stack.push('A')        
my_stack.push('B')        
my_stack.push('C')        

print("pop:",my_stack.pop())
print("peek:",my_stack.peek())
print("isEmpty:",my_stack.isEmpty())
print("size:",my_stack.size)
