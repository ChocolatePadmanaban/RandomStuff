a=.6
b=.4

def probl(a,b):
    return (a**2)*((1-a)**2)*(b**3)*(1-b)

Q1=probl(a,b)/(probl(a,b)+probl(b,a))
Q2=probl(b,a)/(probl(a,b)+probl(b,a))

print(Q1*.5+Q2*.75)
print(Q2*.5+Q1*.75)