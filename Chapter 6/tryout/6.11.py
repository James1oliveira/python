# Create a dictionary called 'cities' with city names as keys
cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'Known as the "City of Light" and famous for the Eiffel Tower.'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'The world’s most populous metropolitan area.'
    },
    'cape town': {
        'country': 'south africa',
        'population': '4.6 million',
        'fact': 'Known for Table Mountain and its beautiful coastline.'
    },
}

# Loop through the dictionary to print information about each city
for city, info in cities.items():
    print(f"\nCity: {city.title()}")

    # Access and print details about the city
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")
