# Extended dictionary with more detailed information about each city
cities = {
    'paris': {
        'country': 'france',
        'population': '2.1 million',
        'fact': 'Known as the "City of Light" and famous for the Eiffel Tower.',
        'landmarks': ['Eiffel Tower', 'Louvre Museum'],
        'famous_food': 'Croissants',
        'language': 'French'
    },
    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'The world’s most populous metropolitan area.',
        'landmarks': ['Tokyo Tower', 'Shibuya Crossing'],
        'famous_food': 'Sushi',
        'language': 'Japanese'
    },
    'cape town': {
        'country': 'south africa',
        'population': '4.6 million',
        'fact': 'Known for Table Mountain and its beautiful coastline.',
        'landmarks': ['Table Mountain', 'Robben Island'],
        'famous_food': 'Bunny Chow',
        'language': 'English, Afrikaans, isiXhosa'
    },
}

# Print a well-formatted travel guide for each city
print("🌍 World Cities Travel Guide 🌍\n")

for city, info in cities.items():
    print(f"{'='*40}")
    print(f"📍 {city.title()}")
    print(f"{'-'*40}")
    print(f"🌐 Country: {info['country'].title()}")
    print(f"👥 Population: {info['population']}")
    print(f"📝 Fun Fact: {info['fact']}")
    print(f"📸 Landmarks: {', '.join(info['landmarks'])}")
    print(f"🍽️ Famous Food: {info['famous_food']}")
    print(f"🗣️ Language(s): {info['language']}")
    print(f"{'='*40}\n")
