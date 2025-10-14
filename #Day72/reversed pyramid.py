rows = 5
 
for i in range(rows,0,-1): 
    # Print leading spaces 
    for space in range(rows - i): 
        print(" ", end="") 
 
    # Print numbers 
    for num in range(1, 2 * i): 
        print(num, end="") 
 
    print()