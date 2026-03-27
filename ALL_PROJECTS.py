# # #n=int(input("CHOOSE A NUMBER??!"))
# # #if n//2==0:
# # #    print("Your number is even!")
# # #else:
# # #    print("Your number is odd!")


# # #Raj1= 6
# # #Raj2= 7
# # #Raj3= 8
# # #Raj4= 20
# # #Raj5= 28

# # #print (Raj1,Raj2,Raj3,Raj4,Raj5)


# # #a="Congratalations!"
# # #print(a.upper())


# # #n=int(input("Choose a number??"))
# # #print(n**0.5)

# # #import turtle as t
# # #t.forward(90)
# # #t.right(90)
# # #t.forward(90)
# # #t.right(90)
# # #t.forward(90)
# # #t.right(90)
# # #t.forward(90)
# # #t.right(90)
# # #t.done()


# # #age=int(input("How old are you??"))
# # #
# # #if age<=20:
# # #    if age>=10:
# # #        print("You are accepted in ages between 10 and 20!")


# # #w=int (input("How many degrees celcius is the weather?"))
# # #
# # #if w>=17:
# # #    print ("Wear light and soft clothes!")
# # #else:
# # #    print ("Wear jackets and pullovers!")

# # c=str(input("Choose a character,numbers or letters?"))
# # if c.isalpha():
# #     print("You have chosen a letter")
# # else:
# #     print("You have not chosen a letter")


# # row=20
# # for py in range (1,row+1):
# #     for j in range (row-py):
# #         print(" ",end="")
# #     for k in range (py):
# #         print("*",end="")
# #     print()


# # num=67
# # b=bin(num).replace("0b","")
# # print(b)


# # n=676767
# # count=0
# # while n>0:
# #     n//=10
# #     count+=1
# # print(count)


# # a=6
# # b=7
# # print(a**b)


# # print(ord("a"))


# _handln
# # d=67
# # print(d*3.14)



# a,b,c=3,4,5
# # print("before swap",a,b,c)
# # a,b,c=c,a,b
# # print("after swap",a,b,c)


# import sys
# def shutdown():
#     print("shutting down program!")
#     sys.exit()
# shutdown()


total=int(input("ENTER THE TOTAL AMOUNT?!"))
G_a=int(input("ENTER THE AMOUNT THE CUSTOMER GAVE?"))
print(G_a-total)