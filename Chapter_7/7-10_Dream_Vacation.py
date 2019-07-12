responses = {}

active = True
while active:
    name = input("\nWhat is your name? ")
    response = input("Where would you go for your dream vacation? ")
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to go to " + response + " for their dream vacation.")
