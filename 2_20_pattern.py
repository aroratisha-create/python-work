#j=int(input("CHOOSE A NUMBER??!"))
#for i in range(j):
#    for hvuyhvlyuhjbnjim in range(i+1):
#        print("*",end="")
#    print()

rows=int(input("How many rows do u want??"))
number=1

for i in range (1,rows +1):
    for j in range(1,i+1):
        print(number,end="")
        number = number + 1
    print()