import random

 

hand=[1,2,3]

score = 0
evil_score = 0


while score  < 3 and evil_score < 3:

    print ("press 1 for rock 2 for sicors 3 for paper")

    x=int(input())

    y = (random.choice(hand))
   
    if x == 1:
        print("your choice: rock")
    elif x == 2:
        print("your choice: sicors")
    elif x == 3:
        print("your choice: paper")
    if y == 1:
        print("evil choice: rock")
    elif y == 2:
        print("evil choice: sicors")
    elif y == 3:
        print("evil choice: paper")


    if y == x:
        print("draw")

    elif y == 1 and x == 2 or y == 2 and x == 3 or y == 3 and x == 1:
        evil_score += 1
        print ("you lose")

    elif y == 2 and x == 1 or y == 3 and x == 2 or y == 1 and x == 3:
        score += 1
        print ("you win")

    print ("your score: ", score)
    print ("evil score: ", evil_score)
    