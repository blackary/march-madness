"""
Take advantage of the fact that the teams.json file is entered in the same order as the
first round
"""
import json
from pathlib import Path
from more_itertools import chunked

teams = json.loads(Path("2021/teams.json").read_text())

names = [t["name"] for t in teams]

first_round_pairs = list(chunked(names, 2))

with open("2021/first_round.json", "w") as f:
    json.dump(first_round_pairs, f, indent=4)
