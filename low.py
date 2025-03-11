import random

num = random.randint(2,99)

guess = -1
print ("guess a number betwen 1 and 100 good luck")
        
while guess != num:
    try:
        guess = int(input("input your number here: "))
    except KeyboardInterrupt:
        exit()
    except:
        print("you have to guess a number")
        continue
    

    if guess == num:
        print ("congratulations")
        
    elif guess < num:
        print ("number is higer")

    elif guess > num:
        print ("number is lower")

    