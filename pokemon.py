class Pokemon:
     def __init__(self, element : str, name : str, health : float, defence : float, attack : float):
        self.element = element
        self.name = name 
        self.health = health
        self.defence = defence
        self.attack = attack



alvin = Pokemon("fire", "alvin", 100, 50, 20)
elon_musk = Pokemon("watta", "elon", 200, 35, 10) 
gabbe = Pokemon("grass", "gabbe", 50, 10, 10) 


def calc_damage(attacker : Pokemon, defender : Pokemon):
    effect = 1
    if attacker.element == "fire" and defender.element == "grass":
        effect = 2
    elif attacker.element == "grass" and defender.element == "watta":
        effect= 2
    elif attacker.element == "watta" and defender.element == "fire":
        effect = 2
    elif attacker.element == "grass" and defender.element == "fire":
        effect = 0.5
    elif attacker.element == "watta" and defender.element == "grass":
        effect = 0.5
    elif attacker.element == "fire" and defender.element == "watta":
        effect = 0.5


    return 50*(attacker.attack/defender.defence) * effect


result = calc_damage(alvin,gabbe)
print(result)

