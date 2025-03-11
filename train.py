import random

class Passenger:
    def __init__(self, name : str, destination : int):
        self.name = name
        self.destination = destination

class Wagon:
    def __init__(self, passengers : list[Passenger]):
        self.passengers = passengers
    
    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)
        pass


class Train:
    def __init__(self, wagons : list[Wagon], line : int, position : int):
        self.wagons = wagons
        self.line = line
        self.position = position
    
class Station:
    def __init__(self, name : str, passengers : list[Passenger]):
        self.name = name
        self.passengers = passengers
    
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
    
    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)
        pass

class Line:
    def __init__(self, name : str, stops : list[int]):
        self.name = name
        self.stops = stops

stations = [
    Station("Stockholm", []),
    Station("Gothenburg", []),
    Station("Malmö", []),
    Station("Uppsala", []),
    Station("Lund", []),
    Station("Västerås", []),
    Station("Linköping", []),
    Station("Östersund", []),
    Station("Helsingborg", []),
    Station("Norrköping", [])
]

lines = [
    Line("Gröda Linjen", [0, 3, 7, 8, 9]),
    Line("Brunda Linjen", [1, 2, 4, 5, 6])
]

trains = [
    Train([Wagon([]), Wagon([]), Wagon([])], 0, 0),
    Train([Wagon([]), Wagon([]), Wagon([])], 1, 0)
]

names = [
    "Anna", "John", "Maria", "Erik", "Lena", "Oliver", "Sara", "David", "Eva", "Fredrik",
    "Emilia", "Jacob", "Sophia", "Alexander", "Isabelle", "William", "Maja", "Oskar", "Alice", "Liam",
    "Nora", "Max", "Olivia", "Elias", "Hannah", "Lucas", "Moa", "Matilda", "Axel", "Klara",
    "Benjamin", "Filip", "Stella", "Noah", "Elsa", "Simon", "Vera", "Oscar", "Chloe", "Viktor",
    "Tilde", "Johan", "Ingrid", "Levi", "Saga", "Theo", "Julia", "Isak", "Alicia", "Gabriel",
    "Felix", "Alva", "Milo", "Liv", "Rasmus", "Hugo", "Lilly", "Signe", "Samuel", "Tove"
]

################################
# Placerar ut alla passagerare #
################################
for i in range(len(stations)):
    name = random.choice(names)
    destination = 0

    for line in lines:
        for stop in line.stops:
            if i == stop:
                destination = random.choice(line.stops)

    passenger = Passenger(name, destination)
    stations[i].passengers.append(passenger)

for station in stations:
    print(station.passengers[0].name, station.passengers[0].destination)


#############
# Game Loop #
#############

for i in range(10):
    #Kolla om passagerare ska hoppa på
    for train in trains:
        station_position = lines[train.line].stops[train.position]
        #Stationen som tåget står vid
        station = stations[station_position]
        for passenger in station.passengers:
            if passenger.destination != station_position:
                station.remove_passenger(passenger)
                train.wagons[0].add_passenger(passenger)
                
    
    #Kolla om passagerare ska hoppa av
    for train in trains:
        station_position = lines[train.line].stops[train.position]
        station = stations[station_position]
        for passenger in train.wagons[0].passengers:
            if passenger.destination == station_position:
                train.wagons[0].remove_passenger(passenger)
                station.add_passenger(passenger)
                
                
    #Flytta alla tåg 1 steg
    for train in trains:
        line = lines[train.line]
        if train.position < len(line.stops) - 1:
            train.position += 1
        else:
            train.position = 0
        
    
    for i in range(len(stations)):
        for passenger in stations[i].passengers:
            print(f"Passageraren vill till {i} och hamnade på {passenger.destination}")

    
        