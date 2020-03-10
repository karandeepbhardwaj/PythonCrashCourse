
def greetUser():
    """Greet user"""
    print("Hello")

greetUser()

#example of functions using positional and keyword

def make_shirt(size, message = 'Coder'):
    print("You ordered the tshirt of size "+ size + " wiht the message " + message)


make_shirt('Large', 'ek toh hum punjabi upr se cute')

make_shirt(message = 'straight out of punjab' , size = 'Large')

make_shirt('large')


def outFunction():
    def innerFunction():
        return "I am in inner function"
    return(innerFunction())


def build_person(firstName , lastName, age=''):
    person = {'first': firstName, 'last' : lastName}
    if age:
        person['age'] = age
    return person

while True:
    
    print("\nPlease tell me your name and your age:") 
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q': 
        break
    
    l_name = input("Last name: ")
    if l_name == 'q': 
        break

    age = input("Age: ")
    if age == 'q':
        break

formatted_name = build_person(f_name, l_name) 
print("\nHello, " + formatted_name + "!")

formatted_name = build_person(f_name, l_name, age) 
print("\nHello, " + formatted_name + "!")


def make_album(name,title,tracks =''):
    person = {
        'name' : name,
        'albumTitle' : title}

    if tracks:
        person['tracks'] = tracks

    return person

while True:

    print("We would like to have the information:")

    artistName = input("\nPlease Enter the artists name:\n")
    albumTitle = input("\nPlease enter the album title:\n")



    album = make_album(artistName, albumTitle)
    print("\nFollowing is the stored information:\n")
    print(album['name'] + " " + album['albumTitle'])

    continueFurther = input("Would you like to make another album? (YES/NO)")

    if continueFurther.lower() == 'no':
        break

#if the person doesnt know how many arguments to pass, then add astrik, it will make a tuple

def make_pizza(*toppings):
    for topping in toppings:
        print(topping)

make_pizza('peperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

#an example to show how function in python accepts the keyword arguements with double asteriks

def build_profile(firstName, lastName, **userInfo):
    profile = {}
    profile['first_name'] = firstName
    profile['last_name'] = lastName
    for key,value in userInfo.items():
        profile[key] = value
    return profile

# call to function to test

print(build_profile("Karandeep", "Bhardwaj", location = "Montreal", university = "Concordia"))