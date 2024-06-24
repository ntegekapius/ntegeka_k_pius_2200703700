#reading and writing files

#polymorphism
#polymorphism allows objects of different classes to be treated as objects of a common superclass

#method resolution order
#method resolution order is order in which python looks for a method in an hierachy classes

#example2: how polymorphism works in python
class Animal:
    def speak(self):
       return "Mweeeeee"
    
class Dog(Animal):
    def speak(self):
        return "Barks"
        
class Cat(Animal):
    def speak(self):
        return "meow"
    
def make_animal_speak(animal):
        print (animal.speak())

make_animal_speak(Dog())
make_animal_speak(Cat())

#Exercise1: create a simple application to manage different types of vehicles.implement derived classe to demonstrate inheritance and polymorphism
#requirements you need are the base class which is vehicle then attributes are make, model and year then methods are display_info() then for the derived classes which is car which inherrits from vehicle then its attributes are number_of_doors,and overrides are display_info()and then other derived class is motorcycle which in herrits from vehicle and its attributes are type_of_byke(cruiser, sport, touring) and overrides are display_info()
#exercise two
#for polymorphism create a function that accepts the list of vehicle objects and call their display_info()method to print details of each vehicle

# Base class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Info: {self.year} {self.make} {self.model}")

# Derived class: Car
class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}, Doors: {self.number_of_doors}")

# Derived class: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        print(f"Motorcycle Info: {self.year} {self.make} {self.model}, Type: {self.type_of_bike}")

# Polymorphic function
def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()

# Example usage
if __name__ == "__main__":
    car = Car("Toyota", "Camry", 2020, 4)
    motorcycle = Motorcycle("Yamaha", "MT-07", 2021, "Sport")

    vehicles = [car, motorcycle]

    display_vehicle_info(vehicles)

"""
working with text files
handling CSV files
JSON and XML file processing
"""
#1. working with text files,open,read, write, and close
#note: python provides inbuilt functions to handle text files
#key concepts
"""--description
opening file: open() function(r, w, a, r+)
reading file: read() function
writing file: write() function
closing file: close() function
"""
#example3: write a file and read a file

#writing to a text file
with open('steka.txt','w') as file:
    file.write('hello am steka and i lov python.\n')
    file.write('I use python for machine learning')

#reading from a text file
with open('steka.txt','r') as file:
    content = file.read()
    print(content)

#handling CSV files
"""
CSV (common seperated values) file widely for data exchange
key concepts
reading CSV files: using 'csv.reader()'
writing CSV files: using 'csv.writer()'
Dictreader and Dictwriter: the class read and write CSV files as dictionaries
"""    