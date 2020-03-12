
# filename = "guest.txt"

# message = input("Hello, Welcome to world of programming, Please tell us your name?")

# with open(filename, 'w') as file_object:
#     file_object.write(message)

# filename2 = "guest_book.txt"
# have_more = True
# count = 0
# while(have_more):
#     message = input("Hello, Welcome to world of programming, Please tell us your name?\n")
#     print("Hello, "+ message.title()+ "!")
#     if count < 1:
#         with open(filename2, 'w') as file_o:
#             file_o.write(message.title()+ " checked in the hotel.\n")
#             count+=1
#     else:
#         with open(filename2, 'a') as file_o1:
#             file_o1.write("\n"+ message.title()+ " checked in the hotel.\n")

#     continue_further = input("Would you like to continue? (Y/N)")
#     if(continue_further.lower() == "n"):
#         have_more = False


filename2 = "responses.txt"
more_people = True
count = 0

while(more_people):

    message = input("Tell us why do you like the programming language you work in?\n")
    if count < 1:
        with open(filename2, 'w') as file_o:
            count+=1
            file_o.write("Response "+str(count) + " " + message +"\n")
            
    else:
        with open(filename2, 'a') as file_o1:
            count+=1
            file_o1.write("Response "+str(count) + " " + message+"\n")

    continue_further = input("Would you like to continue? (Y/N)")
    if(continue_further.lower() == "n"):
        more_people = False
