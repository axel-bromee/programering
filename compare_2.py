#first sum loop
def getSum(x): 
    z = 0
    for y in str(x):  
      z += int(y)       
    return z

#the inputs
b = input("first number:" )
first_sum = getSum(b)
a = input("second number:" )
second_sum = getSum(a)


#prints the number sum just so you can see it
print ("first sum:")
print(first_sum)
print ("second sum:")
print(second_sum)

#just for conviniense
print ("do they match")

#prints true or false depending on if the sum is the same or not
if second_sum == first_sum:
   print("True")

else:
   print("False")
