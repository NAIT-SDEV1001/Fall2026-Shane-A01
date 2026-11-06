#Object oriented programming (OOP)
#uses classes to model real world things
#A class is a blueprint for each object instantiated/created from the class
#Each object will have its own copy of attributes from the class
class Car:
    #constructor method
    #Runs when you instantiate an object
    #used to define attributes when the object is instantiated
    #self refers the object calling the method
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._speed = 0

    def Honk(self):
        print(f'{self.make}, {self.model} says Beep Beep')

    def accelerate(self, amount):
        self._speed += amount

    def decelerate(self, amount):
            self._speed -= amount

    #override the __str__() to return what we want
    def __str__(self):
         return f'The {self.year} {self.make}, {self.model} is travelling at {self._speed} km/h'
    #__repr__ is used for testing and debugging
    def __repr__(self):
        return f"Car('{self.make}', '{self.model}',{self.year})"
          
def main():
    # instantiate 3 cars
    car1 = Car('Ford','F150',2020)
    car2 = Car('Mazda','3',2017)
    car3 = Car('VW','Rabbit',1991)
    
    #access the attributes
    print(car2.make)
    car2.make = 'Tesla'
    print(car2.make)
    #python allows additional attributes on objects
    car3.seats = 4
    print (car3.seats)

    #Honk
    car1.Honk()
    car2.Honk()

    car1.accelerate(50)
    print(car1._speed)
    car1.accelerate(200)
    print(car1._speed)

    #what happens when you print an object? displays its memory location. Useless!
    #when you print an object it calls __str__(). This method returns the memory location. We will override that method to return what we want.
    print(car1)

    #what does __repr__ return
    print(repr(car1))

if __name__ == '__main__':
    main()