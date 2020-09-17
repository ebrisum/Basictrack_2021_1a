""""
distance:

input: int or float

typeTrans:
input: str

speedCar:
meters

Speedwalk:
meters
"""

distance = float(input('Enter amount of km to destination: '))
typeTrans = input('Enter type of transport (Walking/Car): '.lower())

#Speed of different types of transport:
speedCar = 80
speedWalk = 5

#printing time of different types of transport:
walking = round(distance/ speedWalk, 1)
car = round(distance / speedCar, 1)

if typeTrans == 'walking':
    print("You have to walk", walking*60 , "minutes")
else:
    print("You have to drive", car*60, "minutes")




