import json

def number_reader():
    filename = 'numbers.json'
    with open(filename) as fileObject:
        numbers = json.load(fileObject)
        print(numbers)

number_reader()