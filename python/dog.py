class Dog():

    def __init__(self, name, age):
        
        self.name = name
        self.age = age
    
    def sit(self):

        print(self.name.title() + " is now sitting")

    def roll_over(self):

        print(self.name.title() + " rolled over")

#making an instance of a class

my_dog = Dog('tommy', 6)
your_dog = Dog('sherru',4)

def dog_info(o):
    print("My Dog's name is " + o.name.title() + " and his age is " + str(o.age))
    o.roll_over()
    o.sit()

dog_info(my_dog)
dog_info(your_dog)