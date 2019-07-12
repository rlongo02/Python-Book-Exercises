jake = {'name': 'jake', 'animal': 'dog', 'owner': 'chris', 'g': 'm'}
chloe = {'name': 'chloe', 'animal': 'dog', 'owner': 'sarah', 'g': 'f'}
sophie = {'name': 'sophie', 'animal': 'cat', 'owner': 'robert', 'g': 'f'}
oliver = {'name': 'oliver', 'animal': 'cat', 'owner': 'rebecca', 'g': 'm'}
gracie = {'name': 'gracie', 'animal': 'cat', 'owner': 'abigail', 'g': 'f'}
pets = [jake, chloe, sophie, oliver, gracie]

for pet in pets:    
    if pet['g'].lower() == 'm':
        pro = "He"
    elif pet['g'].lower() == 'f':
        pro = "She"
    print("This pet's name is " + pet['name'].title() + ".")
    print(pro + " is a " + pet['animal'] + " and is owned by " + pet['owner'].title() + ".\n")

