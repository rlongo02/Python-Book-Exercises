def city_country(city_name, country_name):
    formatted = city_name.title() + ', ' + country_name.title()
    return formatted

city = city_country('paris', 'france')
print(city)

city = city_country('tokyo', 'japan')
print(city)

city = city_country('ontario', 'canada')
print(city)
