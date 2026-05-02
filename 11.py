for i in range(1,6):
    for j in range(i,5):
        print(" ", end = " ")
    for j in reversed(range(1,i)):
      print(j+1, end = " ")
    for j in range(i):
        print(j+1, end = " ")  
    print(" ")    

    