number = input()

numbers = []


for i in range(len(number) - 1):
    if(i % 2 == 0):
        numbers += str(int(number[i]) * 2)
    else:
        numbers += number[i]

sum = 0
for num in numbers:
    sum += int(num)

controll_number = (10 - (sum % 10)) % 10

print (controll_number)
lastnumber = int(number[-1])
gender = int(number[-2])

if controll_number == lastnumber :
    print ("right")
else:
    print ("wrong")

if(gender % 2 == 0):
    print ("female")
else:
    print ("male")

if len(number) == 10:
    print ("true")
else:
    1 + str(1)