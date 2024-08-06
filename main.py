import requests
import random

print(random.choice(requests.get('https://raw.githubusercontent.com/robonamari/meme-database/main/URL.json').json()['links']))
