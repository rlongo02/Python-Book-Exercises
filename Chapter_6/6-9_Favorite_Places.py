SF = ['New York', 'Vienna']
TB = ['Williamsburg', 'Madrid']
AC = ['El Salvador', 'Orlando']
favorite_places = {'sarah': SF, 'tiffany': TB, 'alexis': AC}

for name, places in favorite_places.items():
    print(name.title() + "'s favorite places are " + places[0] + " and " + places[1] + ".")

