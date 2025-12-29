class Person():
    def say_hi(self):
        print("Hello, how are you?")

p = Person()
p.say_hi()

#The previous 2 lines can also be written as 
Person().say_hi()

# Notice that the say_hi() method takes no parameters but still has the self in 
# the definition