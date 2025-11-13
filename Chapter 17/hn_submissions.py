from operator import itemgetter  # For sorting dictionaries by a specific key
import requests                  # For making HTTP requests to APIs

# --- Make an API call to get top story IDs ---
url = "https://hacker-news.firebaseio.com/v0/topstories.json"  # Endpoint for top story IDs
r = requests.get(url)  # Send GET request
print(f"Status code: {r.status_code}")  # Print HTTP status code (200 = success)

# Get the list of top story IDs from the response
submission_ids = r.json()

# Prepare a list to store information about each submission
submission_dicts = []

# Process the first 5 submissions for demonstration
for submission_id in submission_ids[:5]:
    # Make a new API call for each submission to get its details
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")  # Show status of each request

    # Convert JSON response to a Python dictionary
    response_dict = r.json()

    # Build a dictionary with relevant info for each submission
    submission_dict = {
        'title': response_dict['title'],  # Article title
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",  # Direct HN link
        'comments': response_dict['descendants'],  # Number of comments
    }

    # Add this submission's info to the list
    submission_dicts.append(submission_dict)

# Sort the submissions by number of comments, descending
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Display the sorted submissions
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
