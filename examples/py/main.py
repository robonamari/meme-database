import random

import requests  # pip install requests==2.32.3

print(
    random.choice(
        requests.get("https://meme-database.robonamari.com/database.json").json()[
            "links"
        ]
    )
)
