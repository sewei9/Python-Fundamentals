import math

# Zwei Funktionen


def mw1(a, b):  # Arithmetischer Mittelwert
    c = (a+b)/2
    return c


def mw2(a, b):       # Geometrischer Mittelwert
    c = math.sqrt(a*b)
    return c


# eval
for i in 1, 2:
    t = "mw" + str(i) + "(3,4)"
    c = eval(t)
    print(c)
print()

# exec
for i in 1, 2:
    t = "print(mw" + str(i) + "(3,4))"
    exec(t)
