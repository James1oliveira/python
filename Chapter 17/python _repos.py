import requests  # For making HTTP requests to APIs

# --- Make an API call to search GitHub repositories ---
url = "https://api.github.com/search/repositories"  # GitHub search endpoint
# Add query parameters:
# - language:python → only Python repos
# - sort:stars → sort by number of stars
# - stars:>10000 → only repos with more than 10,000 stars
url += "?q=language:python+sort:stars+stars:>10000"

# Set headers to specify GitHub API version
headers = {"Accept": "application/vnd.github.v3+json"}
import requests
# Make an API call and check the response.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Convert the response object to a dictionary.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
#Examine the first repository.
repo_dict = repo_dicts[0]
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
 print(f"\nName: {repo_dict['name']}")
 print(f"Owner: {repo_dict['owner']['login']}")
 print(f"Stars: {repo_dict['stargazers_count']}")
 print(f"Repository: {repo_dict['html_url']}")
 print(f"Description: {repo_dict['description']}")
# Send GET request
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")  # 200 = success

# --- Convert response to a Python dictionary ---
response_dict = r.json()  # Parse JSON response

# Total number of repositories matching the query
print(f"Total repositories: {response_dict['total_count']}")

# Check if the results are complete or incomplete
print(f"Complete results: {not response_dict['incomplete_results']}")

# --- Explore information about the repositories ---
repo_dicts = response_dict['items']  # List of repository dictionaries returned
print(f"Repositories returned: {len(repo_dicts)}")  # Usually limited by GitHub API (default 30)

# Examine and print selected information for each repository
print("\nSelected information about each repository:")

for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")                    # Repository name
    print(f"Owner: {repo_dict['owner']['login']}")          # Owner's username
    print(f"Stars: {repo_dict['stargazers_count']}")        # Number of stars
    print(f"Repository: {repo_dict['html_url']}")           # URL to the repo
    print(f"Description: {repo_dict['description']}")       # Repo description
