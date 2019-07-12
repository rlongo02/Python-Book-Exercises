TB = {'fname': 'Tiffany', 'lname': 'Bixler', 'gender': 'f', 
            'age': 17, 'city': 'Glen Burnie'}
AC = {'fname': 'Alexis', 'lname': 'Castillo', 'gender': 'f', 
            'age': 16, 'city': 'Pasadena'}
RB = {'fname': 'Ryan', 'lname': 'Boyer', 'gender': 'm', 
            'age': 17, 'city': 'Glen Burnie'}
people = [TB, AC, RB]

for person in people:    
    if person['gender'].lower() == 'm':
        pro = "He"
    elif person['gender'].lower() == 'f':
        pro = "She"
    print("This person's name is " + person['fname'] + " " + person['lname'] + ".")
    print(pro + " is " + str(person['age']) + " years old and lives in " + person['city'] + ".\n")

