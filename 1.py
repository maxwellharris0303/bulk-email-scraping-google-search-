import geonamescache

def get_cities_in_india():
    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries()
    cities = [city['name'] for city in gc.get_cities().values() if city['countrycode'] == 'US']
    return cities

cities = get_cities_in_india()
print(cities)
print(len(cities))
for city in cities:
    with open('us_cities.txt', 'a', encoding='utf-8') as file:
        file.write(city + "\n")