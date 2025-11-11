# create a right triangle using (*)
def act19():
    for outer in range(1,11,1): 
        for inner in range(1, outer,1): # print triangle using (*)
            print("*", end=" ") 
        print() # to make new line after each row