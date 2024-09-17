
rows = int(input("Enter Size of your square pyramid"))

# Top Triangle
for i in range(rows):
    for j in range(1, rows - i + rows): # Putting Space To the top Part
        print(" ", end=' ')
    for j in range(2 * i+1): # Printing Top
        print("T ", end='')
    print(' ')

# This is upper half
for i in range(1, rows):
    for j in range(rows - i):  # Space before left part
        print(" ", end=' ')
    for k in range(i): # This is right part but only half
        print("R", end=' ')
    for j in range(1,rows*2): # This is Upper half square
        print(" ",end=" ")
    for j in range(i): #Left part of Upper Half
        print("L",end=' ')
    print()

for i in range(rows,0,-1):
    for j in range(rows-i): # Space before Lower Right part
        print(" ",end=' ')
    for k in range(i): # Bottom Right part
        print("R",end=' ')
    for j in range(1,rows*2):
        print(" ",end=" ")  #Bottom Square
    for j in range(i ):
        print("L",end=" ") # Bottom LEft Part
    print()

# Bottom
for i in range(rows,0, -1):
        for k in range(1, rows - i+rows+1):
            print(" ", end=' ')
        for k in range(2 * i - 1):
            print("B", end=' ')
        print(" ")

# Enter Size of your square pyramid5
#                   T  
#                 T T T  
#               T T T T T  
#             T T T T T T T  
#           T T T T T T T T T  
#         R                   L 
#       R R                   L L 
#     R R R                   L L L 
#   R R R R                   L L L L 
# R R R R R                   L L L L L 
#   R R R R                   L L L L 
#     R R R                   L L L 
#       R R                   L L 
#         R                   L 
#           B B B B B B B B B  
#             B B B B B B B  
#               B B B B B  
#                 B B B  
#                   B  



# Enter Size of your square pyramid2
#       T  
#     T T T  
#   R       L 
# R R       L L 
#   R       L 
#     B B B  
#       B  