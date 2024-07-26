import requests
import random

print(random.choice(requests.get('https://raw.githubusercontent.com/robonamari/meme-api/main/URL.json').json()['links']))
