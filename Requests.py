import requests

# Making a GET request
response = requests.get("https://api.github.com")
print("Status Code:", response.status_code)
