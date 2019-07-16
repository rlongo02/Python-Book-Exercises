from restaurant import Restaurant

my_restaurant = Restaurant('alamo cafe', 'mexican food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

my_restaurant.set_number_served(15)
my_restaurant.describe_restaurant()

my_restaurant.increment_number_served(10)
my_restaurant.describe_restaurant()
