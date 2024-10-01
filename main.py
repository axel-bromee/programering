
def addition(x,y):
    return(x+y)

def subtraction(x,y):
    return(x-y)

def multiplikation(x,y):
    return(x*y)

def divition(x,y):
    return(x/y)

print ("välkommen till miniräknaren mata in ett tall")
x =int(input ())
print ("ett till tal")
y =int(input ())

print ("1,addition 2,subtraction 3,multiplication 4,divition")
z =int(input ())
if z == 1:
    summa_a = addition(x,y)
    print(summa_a)
elif z == 2:
    summa_s = subtraction(x,y)
    print(summa_s)
elif z == 3:
    summa_m = multiplikation(x,y)
    print(summa_m)
else:
    summa_d = divition(x,y)
    print(summa_d)


