import requests

# Replace with your GitHub personal access token
access_token = ""
owner = ""
repo = ""

url = f"https://api.github.com/repos/{owner}/{repo}"

headers = {
    "Authorization": f"token {access_token}",
    "Accept": "application/vnd.github.v3+json",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    repository_info = response.json()
    # Extract and work with the settings or other data as needed
    print(repository_info)
else:
    print(f"Failed to retrieve repository settings. Status code: {response.status_code}")
