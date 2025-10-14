rows = 10 
for i in range(1,rows+1): 
    # Print leading spaces 
    for space in range(rows - i): 
        print(" ", end="") 
    # Print stars 
    for star in range(2 * i - 1): 
        print("*", end="") 
    print()