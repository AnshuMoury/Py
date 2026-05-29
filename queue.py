# Using List And Array
"""queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print(queue)

# peek
peek = queue[0]
print(peek)

# pop
pop = queue.pop(0)
print(pop)

# After Dequeue
print(queue)

# isEmpty
isEmpty = not bool(queue)
print(isEmpty)

# size
size = len(queue)
print(size)
"""

#Queue Using Class

# class queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self,element):
#         self.queue.append(element)

#     def peek(self):
#         return self.queue[0]

#     def pop(self):
#         return self.queue.pop(0)

#     def isEmpty(self):
#         return len(self.queue) == 0

#     def size(self):
#         return len(self.queue)

# my_Queue = queue()

# my_Queue.enqueue('A')
# my_Queue.enqueue('B')
# my_Queue.enqueue('C')

# print(my_Queue.queue)
# print(my_Queue.peek())
# print(my_Queue.pop())
# print(my_Queue.queue)
# print(my_Queue.isEmpty())
# print(my_Queue.size())


# Using Linked List

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class myQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.Size = 0  
        
    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.Size += 1 

    def dequeue(self):
        if self.isEmpty():
            print("Queue Underflow")
            return -1
        popData = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.Size -= 1 
        return popData
            
    def getfront(self):
        if self.isEmpty():
            print("Queue is empty")
            return -1
        return self.front.data

    def size(self):
        return self.Size

q = myQueue()
    
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
    
print("Dequeue:", q.dequeue())
print("Front:", q.getfront())
print("Size:", q.size())
    
    
        
