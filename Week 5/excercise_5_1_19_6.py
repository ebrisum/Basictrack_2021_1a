layout = "{0:>4}{1:>6}{2:>6}{3:>8}{4:>13}{5:>24}"


print(layout.format("i", "i*1", "i*2", "i*3", "i*4", "i*5","i*6", "i*7", "i*8", "i*9", "i*10"))
for i in range(1,11):
    print(layout.format(i, i*1, "i*2", "i*3", "i*4", "i*5","i*6", "i*7", "i*8", "i*9", "i*10"))
