import random

import requests

print(
    random.choice(
        requests.get("https://meme-database.robonamari.com/database.json").json()["links"]
    )
)
