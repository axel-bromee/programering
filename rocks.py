import random

'''
rock = 1
sicors = 2
paper = 3
'''

hand=[1,2,3]

score = 0
evil_score = 0


while score  < 3 and evil_score < 3:

    print ("press 1 for rock 2 for sicors 3 for paper")

    x=int(input())

    y = (random.choice(hand))
    print (y)



    if y == x:
        print("draw")

    elif y == 1 and x == 2 or y == 2 and x == 3 or y == 3 and x == 1:
        evil_score += 1
        print ("lose")

    elif y == 2 and x == 1 or y == 3 and x == 2 or y == 1 and x == 3:
        score += 1
        print ("win")

    print ("your score", score)
    print ("evil score", evil_score)
    