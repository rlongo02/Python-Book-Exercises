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

class Admin(User):
    def __init__(self, first_name, last_name, age, bio):
        super().__init__(first_name, last_name, age, bio)
        self.privileges = ['can add post', 'can delete post', 'can ban user'
                            'can unban user', 'can edit source']
    
    def show_privileges(self):
        print(self.first_name.title(), "has the following privileges:")
        for privilege in self.privileges:
            print("-", privilege)
        print('')
        
admin = Admin('justin', 'serota', 28, 'Former Comp Sci Teacher')
admin.show_privileges()
