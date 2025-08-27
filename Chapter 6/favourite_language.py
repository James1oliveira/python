# Create a dictionary of people's favorite programming languages (single language per person)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# Loop through only the keys (names) in the dictionary
for name in favorite_languages.keys():
    # Print each name with the first letter capitalized
    print(name.title())

# Loop through each key-value pair in the dictionary
for name, language in favorite_languages.items():
    # Print a nicely formatted message showing each person's favorite language
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Access Sarah's favorite language and format it properly
language = favorite_languages['sarah'].title()

# Print a message showing Sarah's favorite language
print(f"Sarah's favorite language is {language}.")

# List of specific friends
friends = ['phil', 'sarah']

# Loop through all the names in the dictionary
for name in favorite_languages.keys():
    # Print a simple greeting
    print(f"Hi {name.title()}.")

    # If the person is in the friends list, print a personalized message
    if name in friends:
        # Get the person's favorite language and capitalize it
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# Check if 'erin' is NOT one of the people who took the poll
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Loop through the names in the dictionary, sorted alphabetically
for name in sorted(favorite_languages.keys()):
    # Thank each person for taking the poll
    print(f"{name.title()}, thank you for taking the poll.")

# Print a heading before listing all languages
print("The following languages have been mentioned:\n")

# Loop through all values (languages) in the dictionary (may contain duplicates)
for language in favorite_languages.values():
    # Print each language with the first letter capitalized
    print(language.title())

# Use a set to remove duplicates and print each unique language
for language in set(favorite_languages.values()):
    print(language.title())

# Updated dictionary: now each person can have multiple favorite languages (list of languages)
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
}

# Loop through each person and their list of favorite languages
for name, languages in favorite_languages.items():
    # Print the person's name
    print(f"\n{name.title()}'s favorite languages are:")
    
    # Loop through their list of languages and print each one
    for language in languages:
        print(f"\t{language.title()}")
