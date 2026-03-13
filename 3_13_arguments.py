# def total_cal(bill_amount,tip_percent):
#     Total=bill_amount*(1+0.01*tip_percent)
#     print(Total)
# total_cal(67,15)


# def cube(a):
#     return a*a*a
# def berry(a):
#     if a%3==0:
#         return cube (a)
#     else:
#         return False
# print(berry(63))


def factorial(AMA):
    if AMA ==0 or AMA==1:
        return 1 
    else:
        return AMA*factorial(AMA-1)
print(factorial(7))