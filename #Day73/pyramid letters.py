rows = 5 
 
for i in range(1, rows + 1): 
    # Print leading spaces 
    for space in range(rows - i): 
        print(" ", end="") 
 
    # Print letters 
    for j in range(2 * i - 1): 
        print(chr(65 + j), end="") 
 
    print()