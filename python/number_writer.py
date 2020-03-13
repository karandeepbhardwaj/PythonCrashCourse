import json

def file_writer():
    numbers = [1,2,3,4,5,6,7]
    filename = 'numbers.json'
    with open(filename, 'w') as fileobject:
        json.dump(numbers, fileobject)

file_writer()