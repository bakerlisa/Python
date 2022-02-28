# 1. Basic  
for x in range(0, 150):
    print(x)

# 2. Multiples of Five 
for y in range(0,1000):
    if(y % 5 == 0):
        print(y)

# 3. Counting, the Dojo Way
for z in range(0,100):
    #If we have 5 first we'll never get to line % 10: If we want both then we have to writ it like
    if(z % 10 == 0):
        print("Coding Dojo")
    elif(z % 5 == 0):
        print("Coding")

    # #but honestly we get the same results - % 1o never runs SO
    # if(z % 5 == 0 and z % 10 == 0):
    #     print("Coding Dojo Rocks!")
    # elif(z % 10 == 0):
    #     print("Coding Dojo")
    # elif(z % 5 == 0):
    #     print("Coding")

    # # We can run it in their own indivial statements to get the values 
    # if(z % 5 == 0 and z % 10 == 0):
    #     print("Coding Dojo Rocks!")
    # if(z % 10 == 0):
    #     print("Coding Dojo")
    # if(z % 5 == 0):
    #     print("Coding")

# 4. 
num = 0
for a in (range(0,500000)):
    if(a % 2 != 0):
        num+=a
print(num)

# 5. coutning down by 4's
for b in range(2018,0,-4):
    print(b)

# 6. Flexible Counter
lowNum = 13
highNum = 502
mult = 12
for c in range(lowNum,highNum):
    if(c % mult == 0):
        print(c)
