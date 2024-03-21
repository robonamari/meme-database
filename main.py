import requests
import random

links_response = requests.get('https://raw.githubusercontent.com/robonamari/meme-api/main/URL.json')
links_data = links_response.json()['links']
random_link = random.choice(links_data)

print(random_link)
