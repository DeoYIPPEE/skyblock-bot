from dotenv import load_dotenv
import os
from pathlib import Path
import json
import requests

parent = Path.cwd().parent
dotenv_path = f"{parent}/.env"

load_dotenv(dotenv_path=dotenv_path)

HYPIXEL_API_KEY = str(os.getenv("HYPIXEL_API_KEY"))
HYPIXEL_URL = "https://api.hypixel.net/skyblock/v2/bazaar"

response = requests.get(
    HYPIXEL_URL,
    params = {
        "KEY": HYPIXEL_API_KEY
    },
    timeout = 10
)

data = response.json()

if data["success"] == False:
    raise ValueError(f"{data["cause"]}")
with open(f"{parent}/response_data/forge_bz.json", "w") as f:
    json.dump(data, f)
