class Dog:
    """ Represents a dog with a name. """

    # A class variable, counting the number of dogs
    population = 0

    def __init__(self, name):
        """ Initialize the data. """

        self.name = name
        print("\n(Initializing {})".format(self.name))

        # When a puppy is born, it is added to this population count
        Dog.population += 1

    def die(self):
        """ Recording the death of a dog. """

        print("\n{} is no more!!".format(self.name))
        Dog.population -= 1
        if Dog.population == 0:
            print("\n\n{} was the last one.".format(self.name))
        else:
            print("There are still {:d} dogs barking in this area.".format(Dog.population))
    
    def say_hi(self):
        """ Greetings/Barking by the dog. """
        print("Bhon Bho, my masters/acquaintances call me {}. ".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population. """
        print("We have {:d} dog(s) in this area.\n".format(cls.population))

dog1 = Dog("Jackie")
dog1.say_hi()
Dog.how_many()

dog2 = Dog("Tommy")
dog2.say_hi()
Dog.how_many()

print("\n\tDogs can bark here. \n")

print("Unfortunately a dog died in an accident.")

dog1.die()

dog2.die()
Dog.how_many()

