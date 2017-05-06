from __future__ import print_function
import json

import requests

movie_json = """
{
"Title":"Circut",
"Year":"2000",
"Runtime":"130 min",
"Country":"USA"
}
"""

movie_data = json.loads(movie_json)
print(movie_data)
print("Movie title from static json:")
print(movie_data['Title'])
print()

url = 'http://www.omdbapi.com/?y=&plot=short&r=json&t=true&s=silicon'
resp = requests.get(url)
search_results = resp.json()['Search']
print(search_results)

print("Movies with circuit title:")
for m in search_results:
    print(" * " + m['Title'])
