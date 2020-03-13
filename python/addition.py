havemore = True

while(havemore):
    try:
        number1 = int(input("Please enter a number. \n"))
    except ValueError:
        print("Please enter a valid number")
    else:
        try:
            number2 = int(input("Please enter 2nd number. \n"))
        except ValueError:
            print("Please enter a valid number.")
        else:
            print(number1 + number2)
            message = input("Press Q to quit and C to continue\n")
            if message == 'q':
                havemore = False

# havemore = True

# number1 = input("Please enter one number\n")
# number2 = input("Please enter another number\n")

# try:
#     print(number1 + number2)
# except TypeError:
#     print("Please enter valid number.")