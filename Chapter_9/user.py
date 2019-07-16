class User():
    def __init__(self, first_name, last_name, age, bio):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.bio = bio
        self.login_attempts = 0
    
    def describe_user(self):
        print(self.first_name.title(), self.last_name.title(), 
                "is a", str(self.age), "year old user.")
        print("Their biography reads:\n" + self.bio,"\n")

    def greet_user(self):
        print("Hello,", self.first_name.title() +"!\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
