prompt = "\nWelcome to the theater. How old are you?"
prompt += "\nIf you would rather leave, please enter 'quit'.  "
while True:
    age = input(prompt)
    if int(age) <= 3:
        print("Your ticket is free.")
    elif int(age) > 3 and int(age) <= 12:
        print("Your ticket will cost $10.")
    elif int(age) > 12:
        print("Your ticket will cost $15.")
    elif age == 'quit':
        break
