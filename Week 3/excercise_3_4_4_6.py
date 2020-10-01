numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50,
49.9, 45, 44.9, 40, 39.9, 2, 0]

for grade in numbers:
    if grade>=75:
        print(grade,":First")
    if 70<=grade<75:
        print(grade,":Upper second")
    if 60<=grade<70:
        print(grade,":Second")
    if 50<=grade<60:
        print(grade,":Third")
    if 45<=grade<50:
        print(grade,":F1 Supp")
    if 40<=grade<45:
        print(grade,":F2")
    if  grade<40:
        print(grade,":F3")
