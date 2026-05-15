import requests
import json

url = "https://fakestoreapi.com/products"

response = requests.get(url)

data = response.json()

with open("/opt/airflow/raw_data/products_raw.json", "w") as f:
    json.dump(data, f, indent=4)

print("Extract Complete")