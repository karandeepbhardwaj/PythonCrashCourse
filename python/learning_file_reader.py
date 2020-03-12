file_location = 'learning_python.txt'

# with open(file_location) as object:

#     file_data = object.read()
#     print(file_data)

# with open(file_location) as file_object:

#     for line in file_object:
#         print(line)

big_line = ''

with open(file_location) as file_o:

    lines = file_o.readlines()
    for line in lines:
        big_line += line

if 'python' in big_line:
    print(big_line.replace('pytho','PYTHON'))



message = "karandeep"

print(message.replace('karan', 'sharan'))

