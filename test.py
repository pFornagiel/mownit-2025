import requests

# Define the endpoint and parameters
endpoint = "https://en.wikipedia.org/w/api.php"
params = {
  "action": "query",
  "format": "json",
  "titles": "Python (programming language)",
  "prop": "extracts",
  "exintro": True,
  "explaintext": True
}

# Make the request
response = requests.get(endpoint, params=params)
data = response.json()

print(data['query'])
# Extract and print the page content
pages = data["query"]["pages"]
for page_id, page in pages.items():
  print("Title:", page["title"])
  print("Extract:", page["extract"])
  
