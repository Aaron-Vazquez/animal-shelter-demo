import csv

with open("data/animals.csv", newline="", encoding="utf-8") as f:
    animals = list(csv.DictReader(f))

print(f"Total animals: {len(animals)}")
