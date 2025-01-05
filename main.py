import requests

api_key = "5afb535455df492491ba17f47f555d9f"

# The url is a text, so it is stored in a string
url = ("https://newsapi.org/v2/everything?q=tesla&"
       "from=2024-12-05&sortBy=publishedAt&apiKey="
       "5afb535455df492491ba17f47f555d9f")

# requests is the module or the library itself, so it's in the plural form with S
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])