class User():

    def __init__(self, first_name, last_name, gender, email):
        
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.email = email

    def describe_user(self):
        print(self.first_name)
        print(self.last_name)
        print(self.gender)
        print(self.email)

    def greet_user(self):
        print("Hello "+ self.first_name.title())


user1 = User('Karandeep', 'Bhardwaj', 'male', 'karandiip@gmail.com')
user1 = User('Jaya', 'Sachdeva', 'female','jaya9.js@gmail.com')
user1 = User('Megha', 'Bhardwaj', 'female', 'megha@gmail.com')

def print_for_user(o):
    o.describe_user()

