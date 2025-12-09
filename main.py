print("Insert the atomic number of any element. I will tell you where in the periodic table that element is situated. \n")

a = int(input("Atomic Number: \n"))
p = 0
g = 0
if (a >= 57 and a <= 71):
    p = 6
    g = 3
    print("Period: ", p)
    print("Group: ", g)
elif (a >= 89 and a <= 103):
    p = 7
    g = 3
    print("Period: ", p)
    print("Group: ", g)
elif (a > 86):
    p = 7
    if (a - 86 <= 2):
        g = a - 86
    else:
        g = a - 100
    print("Period: ", p)
    print("Group: ", g)
elif (a > 54):
    p = 6
    if (a - 54 <= 2):
        g = a - 54
    else:
        g = a - 68
    print("Period: ", p)
    print("Group: ", g)
elif (a > 36):
    p = 5
    g = a - 36
    print("Period: ", p)
    print("Group: ", g)
elif (a > 18):
    p = 4
    g = a - 18
    print("Period: ", p)
    print("Group: ", g)
elif (a > 10):
    p = 3
    if (a - 10 <= 2):
        g = a - 10
    else:
        g = a
    print("Period: ", p)
    print("Group: ", g)
elif (a > 2):
    p = 2
    if (a - 2 >= 2):
        g = a - 2
    else:
        g = a + 8
    print("Period: ", p)
    print("Group: ", g)
else:
    p = 1
    if (a == 2):
        g = 18
    else:
        g = 1
    print("Period: ", p)
    print("Group: ", g)
    
        
