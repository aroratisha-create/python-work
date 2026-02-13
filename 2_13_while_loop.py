#i=10
#while i<=20:
 #   print(i)
#    i+=1

#n=int(input("enter a number?"))
#sum= 0
#i=1
#while i<= n:
#    sum=sum + i
#    i=i + 1
#    print ("sum=",sum)

while True:
    print("du behöver kolla upp detta orden på median!! hayayayayahahah")


n=int(input("CHOOSE A NUMBER IF U DARE!!??"))
sum=0
t=n
while t>0:
    s=t%10
    sum+=s**3
    t//=10
if sum==n:
    print("ITS AN ARMSTRONG NUMBER!!")
else:
    print("ITS NOT AN ARMSTRONG NUMBER!! MUHHAHAHAAHAHAH! BETTER LUCK NEXT TIME")