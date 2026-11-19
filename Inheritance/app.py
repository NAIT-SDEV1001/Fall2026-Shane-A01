from animal import Dog,Cat,Bird

dog = Dog("Roger","Brown",4,"Poodle")
cat = Cat("Fluffy","Black",4,"striped",10)
bird = Bird("Buddy","Green",2,20)

#create a list of animals
animals = [dog,cat,bird]

#loop through animals having them all make a noise, move, eat
for animal in animals:
    print("-------------")
    print(animal)#use __str__
    animal.make_a_noise()
    animal.move()
    animal.eat()
    #check to see if the animal is a dog(Dog) that has a chase_car()
    if isinstance(animal,Dog): #is the animal object an instance of the Dog class?
        animal.chase_car()
    if isinstance(animal,Cat):
        animal.knock_things_off_ledge()


    