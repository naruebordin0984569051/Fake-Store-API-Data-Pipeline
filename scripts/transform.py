import pandas as pd
import json

with open("/opt/airflow/raw_data/products_raw.json") as f:
    data = json.load(f)

rows = []

for item in data:
    rows.append({
        "title": item["title"],
        "price": item["price"],
        "category": item["category"],
        "rating": item["rating"]["rate"]
    })

df = pd.DataFrame(rows)

df.to_csv(
    "/opt/airflow/transformed/products_clean.csv",
    index=False
)

print("Transform Complete")