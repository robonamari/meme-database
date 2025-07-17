import random

import requests  # pip install requests

print(
    random.choice(
        requests.get("https://meme-database.robonamari.com/database.json").json()[
            "links"
        ]
    )
)
