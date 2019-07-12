#Active Variable
run = True
while run:
    topping = input("\nWhat is a topping you want on your pizza?  ")
    if topping.lower() == 'quit':
        run = False
    else:
        print("I will put " + topping + " on your pizza for you.")
input("\nMove onto the next loop by entering anything.")

#Conditional Test
message = ''
while message != 'quit':
    message = input("\nWhat is a topping you want on your pizza?  ")
    if message.lower() != 'quit':
        print("I will put " + topping + " on your pizza for you.")
input("\nMove onto the next loop by entering anything.")

#Break Statement
while True:
    topping = input("\nWhat is a topping you want on your pizza?  ")
    if topping.lower() == 'quit':
        break
    print("I will put " + topping + " on your pizza for you.")

