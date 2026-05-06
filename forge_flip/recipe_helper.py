import json
from pathlib import Path
from math import floor

def get_table():
    parent = Path.cwd().parent

    with open(f"{parent}/custom_data/forge_recipes.json", "r") as f:
        return json.load(f)
    
def forge_time(t, flags: list):
    t = str(t)
    hours = 0
    j = 0
    for i in range(len(t)):
        if t[i].isalpha() == True:
            ti = int(''.join(t[j:i]))
            j = i+1
            if t[i] == 'd':
                hours += 24*ti
            elif t[i] == 'h':
                hours += ti
            elif t[i] == 's':
                hours += ti/3600

    cooldown_reduction = quick_forge_converter(flags[0])
    cooldown_reduction += 0.25 if flags[1] else 0
    hours = hours * (1-cooldown_reduction)

    return hours

def quick_forge_converter(level: int = 0):
    TimeReductionPercent = min(30, 10 + (level * 0.5) + floor(level/20) * 10)
    return TimeReductionPercent

