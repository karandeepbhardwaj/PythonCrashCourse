
# def greetUser():
#     """Greet user"""
#     print("Hello")

# greetUser()

# #example of functions using positional and keyword

# def make_shirt(size, message = 'Coder'):
#     print("You ordered the tshirt of size "+ size + " wiht the message " + message)


# make_shirt('Large', 'ek toh hum punjabi upr se cute')

# make_shirt(message = 'straight out of punjab' , size = 'Large')

# make_shirt('large')


def outFunction():
    def innerFunction():
        return "I am in inner function"
    return(innerFunction())

    