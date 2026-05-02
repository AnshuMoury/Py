num = 1
n = 4
for i in range(1,6,):
    for j in range(i,6):
        print(" ", end = " ")
    for j in range(i):
        print("*", end = " ")
    for i in range(0,i):
        print(num, end = " ")     
        num += 2
    print(" ")        
            