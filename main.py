from math import pi
for i in range(2, 12):
    x = "pi = {:." + str(i) + "f}"
    print(x.format(pi))
