weekdays = {
    1:"monday",
    2:"tuesday",
    3:"wednesday",
    4:"thursday",
    5:"friday",
    6:"saturday",
    7:"sunday"
}

day = int(input("On which day start your holiday? (1-7): "))
duration = int(input("How many days will your trip take?: "))
index = (duration%7)
print("You will return on a " + weekdays[int(day)+ index])
