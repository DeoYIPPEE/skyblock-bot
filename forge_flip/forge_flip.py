import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path
import forge_flip.recipe_helper as recipe_helper
from forge_flip.retriever import data
#TODO: add a flags thing from the discord bot interaction

data = data

forge_recipes = recipe_helper.get_table()

cost = 0
max_details = []
max = 0
for forged, details in forge_recipes.items():
    for materials, amount in details["materials"].items():
        cost += data["products"][materials]["quick_status"]["buyPrice"] * amount
    sell = data["products"][forged]["quick_status"]["sellPrice"]
    profit = sell - cost
    time = details["forge_time"]
    time = recipe_helper.forge_time(time)
    profit_per_hour = profit / time
    if profit_per_hour > max:
        max = profit_per_hour
        max_details = [forged, details["materials"], max]
    cost = 0
    profit = 0
