import random
import collections

deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

p1_hand = []
p2_hand = []
p3_hand = []

p1_score = 0
p2_score = 0
p3_score = 0

current_player = 0



def deal_cards(player : int):

    for i in range(7):
        card = random.choice(deck)

        if player == 1:
            p1_hand.append(card)
        elif player == 2:
            p2_hand.append(card)
        else:
            p3_hand.append(card)

        deck.remove(card)



def check_if_stack():
    global p1_score
    p1_count = collections.Counter(p1_hand)

    for key, value in p1_count.items():
        if value == 4:
            p1_score += 1
            p1_hand.remove(key)
            p1_hand.remove(key)
            p1_hand.remove(key)
            p1_hand.remove(key)
            print(p1_score)
        


    global p2_score
    p2_count = collections.Counter(p2_hand)

    for key, value in p2_count.items():
        if value == 4:
            p2_score += 1
            p2_hand.remove(key)
            p2_hand.remove(key)
            p2_hand.remove(key)
            p2_hand.remove(key)
            print(p2_score)
        

    global p3_score
    p3_count = collections.Counter(p3_hand)

    for key, value in p3_count.items():
        if value == 4:
            p3_score += 1
            p3_hand.remove(key)
            p3_hand.remove(key)
            p3_hand.remove(key)
            p3_hand.remove(key)
            print(p3_score)
        


deal_cards(1)
deal_cards(2)
deal_cards(3)

while True:
    print ("player 1 turn")
    print ("P1 SCORE",p1_score)
    check_if_stack()
    print (p1_hand)
    print("Choose a player")
    player_choice = input()
    print("Choose a card")
    card_choice = input()

    target_hand = []

    match player_choice:
        case "2": 
            target_hand = p2_hand
        
        case "3":
            target_hand = p3_hand

    
    if card_choice in target_hand:
        print ("here take my : " + card_choice)
        count = collections.Counter(target_hand)
        for card_choice, value in count.items():
            if value == 1:
                p1_hand.append(card_choice)
                target_hand.remove(card_choice)
            elif value == 2:
                p1_hand.append(card_choice)
                p1_hand.append(card_choice)
                target_hand.remove(card_choice)
                target_hand.remove(card_choice)
            elif value == 3:
                p1_hand.append(card_choice)
                p1_hand.append(card_choice)
                p1_hand.append(card_choice)
                target_hand.remove(card_choice)
                target_hand.remove(card_choice)
                target_hand.remove(card_choice)
        
    else:
        card = random.choice(deck)
        print ("go fish")
        print("You got : " + card)
        p1_hand.append(card)
        deck.remove(card)
    
    print ("player 2 turn")
    print ("P2 SCORE",p2_score)
    check_if_stack()
    print (p2_hand)
    print("Choose a player")
    player_choice = input()
    print("Choose a card", p2_hand)
    card_choice = input()

    target_hand = []

    match player_choice:
        case "1": 
            target_hand = p1_hand
        
        case "3":
            target_hand = p3_hand

    
    if card_choice in target_hand:
        print ("here take my : " + card_choice)
        count = collections.Counter(target_hand)
        for card_choice, value in count.items():
            if value == 1:
                p2_hand.append(card_choice)
                target_hand.remove(card_choice)
            elif value == 2:
                p2_hand.append(card_choice)
                p2_hand.append(card_choice)
                target_hand.remove(card_choice)
                target_hand.remove(card_choice)
            elif value == 3:
                p2_hand.append(card_choice)
                p2_hand.append(card_choice)
                p2_hand.append(card_choice)
                target_hand.remove(card_choice)
                target_hand.remove(card_choice)
                target_hand.remove(card_choice)
        
        
    else:
        card = random.choice(deck)
        print ("go fish")
        print("You got : " + card)
        p2_hand.append(card)
        deck.remove(card)


    print ("player 3 turn")
    print ("P3 SCORE",p3_score)
    check_if_stack()
    print (p3_hand)
    print("Choose a player")
    player_choice = input()
    print("Choose a card", p3_hand)
    card_choice = input()

    target_hand = []

    match player_choice:
        case "2": 
            target_hand = p2_hand
        
        case "1":
            target_hand = p1_hand

    
    if card_choice in target_hand:
        print ("here take my : " + card_choice)
        count = collections.Counter(target_hand)
        for card_choice, value in count.items():
            if value == 1:
                p3_hand.append(card_choice)
                target_hand.remove(card_choice)
            elif value == 2:
                p3_hand.append(card_choice)
                p3_hand.append(card_choice)
                target_hand.remove(card_choice)
                target_hand.remove(card_choice)
            elif value == 3:
                p3_hand.append(card_choice)
                p3_hand.append(card_choice)
                p3_hand.append(card_choice)
                target_hand.remove(card_choice)
                target_hand.remove(card_choice)
                target_hand.remove(card_choice)
        
    else:
        card = random.choice(deck)
        print ("go fish")
        print("You got : " + card)
        p3_hand.append(card)
        deck.remove(card)