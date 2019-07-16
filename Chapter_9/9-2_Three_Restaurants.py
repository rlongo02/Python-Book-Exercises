class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("My restaurant's name is " + self.restaurant_name.title() + ".")
        print("My restaurant sells " + self.cuisine_type + ".\n")
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open for the day!\n")
        
my_restaurant = Restaurant('alamo cafe', 'mexican food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant = Restaurant('whataburger', 'fast food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant = Restaurant('charleys', 'grilled subs')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
