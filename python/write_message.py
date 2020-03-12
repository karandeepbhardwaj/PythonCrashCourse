filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

with open(filename) as file_o:
    line = file_o.read()
    print(line)