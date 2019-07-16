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
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry',
                        'mint chocolate chip', 'birthday cake']
    
    def display_flavors(self):
        print("Available Flavors:")
        for flavor in self.flavors:
            print("-", flavor.title())0
        print('')
            
mystand = IceCreamStand("bibi's", 'ice cream')
mystand.display_flavors()
