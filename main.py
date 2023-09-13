"""Main component to perform a search on Bing using the requests library."""

import requests

url = "https://www.bing.com/search?q=oscal"


def perform_search(url):
    try:
        print("Requesting", url)
        response = requests.get(url)
        if response.status_code == 200:
            data = response
            print("API Response:", data)
            return response.status_code
        else:
            print(
                "Error: Request to the API failed with status code",
                response.status_code,
            )
    except requests.exceptions.RequestException as e:
        print("Request Exception:", e)


if __name__ == "__main__":
    perform_search(url)
