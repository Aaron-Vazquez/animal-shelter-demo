import csv
from collections import Counter

with open("data/animals.csv", newline="", encoding="utf-8") as f:
    animals = list(csv.DictReader(f))

print(f"Total animals: {len(animals)}")

status_counts = Counter(animal["status"] for animal in animals)
for status, count in sorted(status_counts.items()):
    print(f"{status}: {count}")
