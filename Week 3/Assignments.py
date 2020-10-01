weekdays = {
    1:"monday",
    2:"tuesday",
    3:"wednesday",
    4:"thursday",
    5:"friday",
    6:"saturday",
    7:"sunday"
}

day = int(input("which day of the week is it?(1-7): "))

if day == 7:
    print("Today it's " + weekdays[int(day)], ",tomorrow it will be", weekdays[1])
else:
    print("Today it's " + weekdays[int(day)]+ ", tomorrow it will be", weekdays[int(day)+1])
