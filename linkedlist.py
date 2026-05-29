class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def transverseandprint(head):
    currNode = head
    while currNode:
        print(currNode.value, end = " -> ")
        currNode = currNode.next
    print("Null")

node1 = Node(1)        
node2= Node(2)        
node3 = Node(3)        
node4 = Node(4)        
node5= Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
transverseandprint(node1)


# Lowest Value
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def lowestValue(head):
  lowestValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < lowestValue:
      lowestValue = currentNode.data
    currentNode = currentNode.next
  return lowestValue

node1 = Node(1)        
node2= Node(2)        
node3 = Node(3)        
node4 = Node(4)        
node5= Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5        
print(lowestValue(node1))                 

# Delete a Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def transverseandprint(head):
    currNode = head
    while currNode:
        print(currNode.data, end = " -> ")
        currNode = currNode.next
    print("Null")        

def deleteNode(head, value):
    if head == value:
        return head.next
    currNode = head
    while currNode and currNode.next != value:
        currNode = currNode.next
        if currNode is None:
            return head
        currNode.next = currNode.next.next
        return head
    
node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
transverseandprint(node1)

# Delete node4
node1 = deleteNode(node1, node4)

print("After deletion:")
transverseandprint(node1)

# Insert a Node
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def transverseandprint(head):
    currNode = head
    while currNode:
        print(currNode.data, end = " -> ")    
        currNode = currNode.next
        print("Null")

def insertNode(head, value, position):
    if position == 1:
        value.next = head
        return value
    currNode = head
    for _ in range (position - 2):
        if currNode.next is None:
            break
        currNode = currNode.next

        value.next = currNode.next

    value.next = currNode.next
    currNode.next = value
    return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4      

value = Node(84)
newValue = insertNode(node1, value, 3)
transverseandprint(node1)