class Student:
    def __init__(self, f_name : str, l_name : str, year : int, grade : list):
        self.f_name = f_name
        self.l_name = l_name
        self.year = year
        self.grade = grade
    
    def __str__(self):
        return f"{self.f_name} {self.l_name}"

    def info(self):
        print(self.f_name, self.l_name, self.year, self.grade)

    def calc_grade(self):
        suma = sum(self.grade)
        suma /= len(self.grade)
        print (suma)

    def add_grade(self):
        x = int(input ("what grade you wanna add: "))
        self.grade.append(x)

class Klassrom:
    def __init__(self, name : str ,gonners : list):
        self.name = name
        self.gonners = gonners
    

    def add_gonners(self):
        self.gonners.append(elev1)
        self.gonners.append(elev2)
        self.gonners.append(elev3)
        print (self.gonners)
    
    def info1(self):
        print(self.name, self.gonners)

 

elev1 = Student("alvin", "Gonnerstar", 2007, [4, 4, 3, 2, 1])
elev2 = Student("axel", "bromee", 2007, [1,2,2,3,4])
elev3 = Student("alfred", "kärnström", 1987, [3,1,7,1,6,1,5,1,])
klass1 = Klassrom("b1", [])
klass1.add_gonners()
elev1.info()
elev1.calc_grade()
elev1.add_grade()
elev1.info()
klass1.info1()

