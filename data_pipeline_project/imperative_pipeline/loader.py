import csv
from datetime import datetime

def load_csv(path):
    rows = []
    with open(path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            rows.append(dict(r))
    return rows
