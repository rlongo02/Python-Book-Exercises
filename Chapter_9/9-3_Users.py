class User():
    def __init__(self, first_name, last_name, age, bio):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.bio = bio
    
    def describe_user(self):
        print(self.first_name.title(), self.last_name.title(), 
                "is a", str(self.age), "year old user.")
        print("Their biography reads:\n" + self.bio,"\n")

    def greet_user(self):
        print("Hello,", self.first_name.title() +"!\n")

user1 = User('robert', 'longo', 17, 'Trumpet player, Actor, Student.')
user2 = User('tiffany', 'bixler', 17, 'Drum Major, FBLA Officer.')
user3 = User('ronan', "o'toole", 17, 'Drama VP, STEM Student.')

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()
