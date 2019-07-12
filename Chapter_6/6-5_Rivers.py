rivers = {
    'neva': 'russia',
    'nile': 'egypt',
    'amazon': 'south america'
    }

for river, country in rivers.items():
    print("The " + river.title() + " flows through " + country.title() + ".")
print("\n")

for river in rivers.keys():
    print(river.title())
print("\n")
    
for country in rivers.values():
    print(country.title())
