class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print("My restaurant's name is " + self.restaurant_name.title() + ".")
        print("My restaurant sells " + self.cuisine_type + " food.\n")
        
    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open for the day!")
        
my_restaurant = Restaurant('alamo cafe', 'mexican')
print(my_restaurant.restaurant_name, ",", my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
