import requests  # For making HTTP requests to APIs
import json      # For formatting JSON data nicely

# --- Make an API call ---
url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"  # URL for a specific Hacker News item
r = requests.get(url)  # Send a GET request to the API
print(f"Status code: {r.status_code}")  # Print HTTP status code (200 = success)

# --- Explore the structure of the data ---
response_dict = r.json()  # Parse the JSON response into a Python dictionary

# Convert the dictionary to a nicely formatted string for readability
response_string = json.dumps(response_dict, indent=4)  # Pretty-print with 4-space indentation
print(response_string)  # Display the structured JSON data
