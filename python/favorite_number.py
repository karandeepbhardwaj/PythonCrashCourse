import json

def favorite_writer():
    number = int(input("Please enter your favorite numbe\n"))
    filename = 'favorite_number.json'
    with open(filename, 'w') as fileObject:
        json.dump(number, fileObject)

def favorite_reader():
    filename = 'favorite_number.json'
    with open(filename) as fileObject:
        content = json.load(fileObject)
        print("I know your favorite number! its " + str(content))

favorite_writer()
favorite_reader()

filename = 'favorite_number.json'

try:
    with open(filename) as fileObject:
        content = json.load(fileObject)
except FileNotFoundError:
    number = int(input("Please enter your favorite numbe\n"))
    with open(filename, 'w') as fileObject:
        json.dump(number, fileObject)
else:
    print("I know your favorite number! its " + str(content))