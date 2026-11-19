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

class Cat(Animal):  # Cat inherits from Animal, including its eat and move methods.
    def __init__(  # Split the parameter list across lines so each parameter is easy to read.
        self,  # Refer to the Cat object being initialized.
        name: str,  # Accept the cat's name as text.
        color: str,  # Accept the cat's colour as text.
        num_legs: int,  # Accept the leg count as an integer.
        pattern: str,  # Accept the cat's coat pattern as text.
        anger_level: int,  # Accept an integer used later to choose the cat's sound.
    ) -> None:  # Finish the signature. __init__ initializes the object and returns None.
        super().__init__(name, color, num_legs)  # Initialize the shared attributes through Animal.
        self.pattern = pattern  # Store the coat pattern on this Cat object.
        self.anger_level = anger_level  # Store the anger level on this Cat object. 

    def __str__(self) -> str:  # Override Animal's display method for cats.
        return (  # Build a single string containing both shared and cat-specific details.
            f"{super().__str__()}\n"  # Start with Animal's display text and add a line break.
            f"Pattern: {self.pattern}\n"  # Add the coat pattern and another line break.
            f"Anger Level: {self.anger_level}"  # Finish with the anger level.
        )  # End the string expression.
    
    def make_a_noise(self) -> None:  # Override Animal's sound and choose a sound based on anger level.
        if self.anger_level < 10:  # Handle anger levels below 10.
            print("Purr purr")  # A low anger level produces a purr.
        elif self.anger_level <= 20:  # The first test already ruled out levels below 10, so this covers 10 through 20.
            print("Meow meow")  # A medium anger level produces a meow.
        else:  # The only remaining integer levels are above 20.
            print("Hiss!")  # A high anger level produces a hiss.

    def knock_things_off_ledge(self) -> None:  # Add a method specific to Cat.
        print(f"{self.name} knocks things off a ledge!")  # Print what this cat is doing.

class Bird(Animal):  # Bird inherits from Animal and overrides several of its behaviours.
    def __init__(  # Define the initializer for a Bird object.
        self, name: str, color: str, num_legs: int, wingspan: float  # Accept the shared details plus a wingspan that can have a fractional part.
    ) -> None:  # Finish the signature. The initializer returns None.
        super().__init__(name, color, num_legs)  # Let Animal initialize the shared attributes on this Bird object.
        self.wingspan = wingspan  # Store the wingspan on this Bird object.

    def __str__(self) -> str:  # Override Animal's display method for birds.
        return f"{super().__str__()}\nWingspan: {self.wingspan}"  # Reuse Animal's display text and add the wingspan on a new line.

    def eat(self) -> None:  # Override Animal's default eating behaviour.
        print(f"{self.name} pecks at the food.")  # Describe how this bird eats.

    def move(self) -> None:  # Override Animal's default movement.
        print(f"{self.name} flies around!")  # Describe how this bird moves.

    def make_a_noise(self) -> None:  # Override Animal's default sound.
        print("I want crackers")  # Print the phrase this example bird says.

def main():
    dog1 = Dog("Rover","Black",4,"Poodle")
    print(dog1.name)
    print(dog1.breed)
    print(dog1)
    dog1.make_a_noise()
if __name__ == "__main__":
    main()