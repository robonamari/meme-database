import random

import requests

print(
    random.choice(
        requests.get("https://meme-database.robonamari.com/URL.json").json()["links"]
    )
)
