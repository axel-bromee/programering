import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
number = ["1","2","3","4","5","6","7","8","9","0"]
spesia = ["!","@","#","£","¤","$","%","&","?","§"]

print ("make your super safe password")
print ("how long")
lengt = int(input ())
print ("do you want capital letters" "\n" "1 for no  2 for yes")
big = int(input())
if big == 2:
    big = True
else:
    big = False
print ("do you want numbers" "\n" "1 for no  2 for yes")
numbers = int(input())
if numbers == 2:
    numbers = True
else:
    numbers = False
print ("do you want spesial carecters" "\n" "1 for no  2 for yes")
spesial = int(input())
if spesial == 2:
    spesial = True
else:
    spesial = False

password = []

while len(password) < lengt:
    ass1 = random.choice(letters)
    ass2 = random.choice(number)
    ass3 = random.choice(spesia)

 
    if (big == True):
        if(random.randint(0,1) == 1):
            ass1 = ass1.upper()
    
    password.append(ass1)

    
    if (numbers == True):
        password.append(ass2)

    if (spesial == True):
        password.append(ass3)

random.shuffle(password)

while(len(password) > lengt):
    password.pop(0)
print (password)