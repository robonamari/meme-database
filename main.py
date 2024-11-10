import requests
import random

print(random.choice(requests.get('https://meme-database.robonamari.com/URL.json').json()['links']))
