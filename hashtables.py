# Creating an Empty List
myList = [None,None,None,None,None,None,None,None,None,None]   #Elements called bucket in hash table

# Creating a Hash function
def hashfunction(value):
    sum_of_char = 0
    for char in value:
        sum_of_char += ord(char)
    return sum_of_char % 10

print(hashfunction("Bob"))

# Inserting a element
def add(name):
    index = hashfunction(name)
    myList[index] = name

add("Bob")
print(myList)     

# Looking up a name 
def contains(name):
    index = hashfunction(name)
    return myList[index] == name 
print(contains("Bob"))
    

#Handeling Collisions 
list = [[],[],[],[],[],[],[],[],[],[]]

def append(name):
    index = hashfunction(name)
    list[index].append(name)
append("Bob")    
append("Pete")    
append("Jones")    
append("Lisa")    
append("Siri")    
print(list)