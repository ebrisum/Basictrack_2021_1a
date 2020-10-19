a = 4
b = 3
c = 5

if a>c:
    a, c = c, a

if b>c:
    b, c = c, b

hypotenuse = (a * b + b * b) ** .5

if abs(c-hypotenuse) < 1e-7:
    print("The triangle is right-angled")
else:
    print("This is not a right-angled triangle")

