#i= 1
#while i<=5:
#    j=1
#    while j<=10:
#        print(j,end="")
#        j=j+1
#    i=i+1
#    print()

#i=input("HEYY!! WHAT IS UR NAME!!?")
#j=input("WHICH LETTER IN UR NAME WOULD U LIKE TO CHOOSE??")
#a= 0
#c= 0
#while a<len(i):
#    if i[a]==j:
#        c= c+1
#    a=a+1
#print(c)

l=int(input("Choose the lowest number?"))
h=int(input("Choose the highest number?"))

for i in range(l,h+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
