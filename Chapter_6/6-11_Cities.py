SA = {'country': 'the united states', 'population': '1.493 million', 'fact': 'home to the Alamo'}
CS = {'country': 'the united states', 'population': '464,474', 'fact': 'my birthplace'}
GB = {'country': 'the united states', 'population': '69,499', 'fact': 'where my school is'}

cities = {'san antonio': SA, 'colorado springs': CS, 'glen burnie': GB}

for name, info in cities.items():
    print(name.title() + " is a city in " + info['country'] + " and has a population of " + info['population'] + " people.")
    print("Fun fact: it is " + info['fact'] + '.\n')
