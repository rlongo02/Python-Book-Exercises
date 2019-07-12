person = {'fname': 'Tiffany', 'lname': 'Bixler', 'gender': 'f', 
            'age': 17, 'city': 'Glen Burnie'}

if person['gender'].lower() == 'm':
    pro = "He"
elif person['gender'].lower() == 'f':
    pro = "She"

print("This person's name is " + person['fname'] + " " + person['lname'] + ".")
print(pro + " is " + str(person['age']) + " years old and lives in " + person['city'] + ".")
