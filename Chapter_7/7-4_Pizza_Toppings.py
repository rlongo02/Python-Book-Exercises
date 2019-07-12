run = True
while run:
    topping = input("\nWhat is a topping you want on your pizza?  ")
    if topping.lower() == 'quit':
        run = False
    else:
        print("I will put " + topping + " on your pizza for you.")
