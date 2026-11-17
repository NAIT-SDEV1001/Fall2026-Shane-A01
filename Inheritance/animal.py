class Animal:
    def __init__(self, name:str, color:str, num_legs:int)->None:
        self.name = name
        self.color = color
        self.num_legs = num_legs

    def __str__(self)->str:#placing () around our return return string will allow us to write it as follows
        return (
            f"Name: {self.name}\n"
            f"Color: {self.color}\n"
            f"Number of Legs: {self.num_legs}\n"
            )

    def eat(self)->None:
        print(f"{self.name} starts eating. Yum Yum!")

    def make_a_noise(self)->None:
        print(f"{self.name} makes an interesting noise")

    def move(self)->None:
        print(f"{self.name} runs around")

#inherit from Animal
class Dog(Animal):
    def __init__ (self, name:str, color:str, num_legs:int, breed:str)->None:
        #pass the constructor values into the parent classes (Animal) constructor
        #super() refers to the parent class
        super().__init__(name,color,num_legs)
        #add an attribute specific to dogs
        self.breed = breed

    def __str__(self)->str:
        #call the __str__ from Animal to get name, color, num_legs 
        # f"Name: {self.name}\n"
        # f"Color: {self.color}\n"
        # f"Number of Legs: {self.num_legs}\n"
        return_string = super().__str__()
        #append(string concatonation) breed to that string
        return_string += f"Breed: {self.breed}\n"
        #results in
        # f"Name: {self.name}\n"
        # f"Color: {self.color}\n"
        # f"Number of Legs: {self.num_legs}\n"
        # f"Breed: {self.breed}\n"
        return return_string

    def chase_car(self)->None:
        print(f"{self.name} chases a car!")
    #This method will be called for dogs (overrides the same method in Animal)
    def make_a_noise(self)->None:
            print(f"{self.name} starts barking! Woof Woof")

def main():
    dog1 = Dog("Rover","Black",4,"Poodle")
    print(dog1.name)
    print(dog1.breed)
    print(dog1)
    dog1.make_a_noise()
if __name__ == "__main__":
    main()