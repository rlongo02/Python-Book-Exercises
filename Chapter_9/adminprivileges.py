from user import User 
class Admin(User):
    def __init__(self, first_name, last_name, age, bio):
        super().__init__(first_name, last_name, age, bio)
        self.privileges = Privileges()    
        
class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user'
                            'can unban user', 'can edit source']
                            
    def show_privileges(self):
        print("This user has the following privileges:")
        for privilege in self.privileges:
            print("-", privilege)
        print('')

