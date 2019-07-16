class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name.title() + ".")
        print("This restaurant sells " + self.cuisine_type + ".")
        print("It has served " + str(self.number_served) + " customers.\n")
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open for the day!\n")
        
    def set_number_served(self, served):
        self.number_served = served
        
    def increment_number_served(self, customers):
        self.number_served += customers
        
my_restaurant = Restaurant('alamo cafe', 'mexican food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(15)
my_restaurant.describe_restaurant()

my_restaurant.increment_number_served(10)
my_restaurant.describe_restaurant()
