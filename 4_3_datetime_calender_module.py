#  import datetime
#  s=datetime.datetime.now()
#  print(s)

#  import calendar
#  # print(calendar.month(2026,12))

#  import calendar
#  t=calendar.Calendar(firstweekday=11)
# print(list(t.iterweekdays()))


# from datetime import date,time,datetime
# s=datetime.now()
# print(date.today())
# print(s)


# import random #importing module
# import time

# def getRandomDate(startDate, endDate ): #defining function
#     print("Printing random date between", startDate, " and ", endDate)
#     randomGenerator = random.random()
#     dateFormat='%m/%d/%Y'
    
#     startTime = time.mktime(time.strptime(startDate, dateFormat))
#     endTime = time.mktime(time.strptime(endDate, dateFormat))
#     randomTime = startTime + randomGenerator * (endTime - startTime)
#     randomDate = time.strftime(dateFormat, time.localtime(randomTime))
#     return randomDate


# print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))



# def hotel_cost(nights):
#     return 140*nights


# def plane_ride_cost(city):
#     if "Charlotte" == city:
#         return 183
    
#     elif "Tampa" == city:
#         return 220
    
#     elif "Pittsburgh" == city:
#         return 222
    
#     elif "Los Angeles" == city:
#         return 475


# def rental_car_cost(days):
#     if days>=7 :
#         return 40*days - 50
    
#     elif days>=3 :
#         return 40*days - 20
    
#     else:
#         return 40*days


# def trip_cost(city, days, spending_money):
#     return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


# print("Cost of car rental: ",rental_car_cost(5))

# print("Cost of plane ride: ",plane_ride_cost("Los Angeles"))

# print("Cost of hotel room: ", hotel_cost(7))

# print("Total cost of the trip:",trip_cost("Los Angeles",7,500))

# print(trip_cost("Tampa",6,500))