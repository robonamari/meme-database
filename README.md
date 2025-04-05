<div align="center">

[**Other Languages**](.github/README/)
</div>

<p align="center">
    <img src="https://img.shields.io/github/languages/code-size/robonamari/meme-database?style=flat" alt="Code Size">
    <img src="https://tokei.rs/b1/github/robonamari/meme-database?style=flat" alt="Total lines">
    <img src="https://img.shields.io/badge/all%20languages-all%20Versions-blue" alt="All Versions">
    <img src="https://img.shields.io/github/license/robonamari/meme-database" alt="GitHub license">
</p>

---

This project contains a collection of Iranian memes presented in a JSON file. This collection can be utilized in various applications and services to display content to users.

## Features
- Fetching content from an online JSON database.
- Only contains short links for quick access.

| Picture | Video  | Text | Gif    | total  |
| ------- | ------ | ---- | ------ | ------ |
| 632     | 1902   | :x:  | :x:    | 2534   |

## Help
An exmaple to gather links with python:
```python
import random

import requests # pip install requests==2.32.3

print(
    random.choice(
        requests.get("https://meme-database.robonamari.com/database.json").json()["links"]
    )
)
```

## Sources
* [MoonFall Discord Server](https://discord.gg/BsaC3QgEQz)
* [Roz Sorkh 🌹 Discord Server](https://discord.gg/a7jbGR99bW)
