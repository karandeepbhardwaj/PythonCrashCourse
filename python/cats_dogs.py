def catsdogs(file):

    try:
        with open(file) as fileObject:
            content = fileObject.read()
    except FileNotFoundError:
        # print("There is no such file named as "+ str(file))
        pass
    else:
        print(content)

files = ['cats.txt', 'dogs.txt']

for file in files:
    catsdogs(file)