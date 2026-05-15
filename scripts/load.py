import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv(
    "/opt/airflow/transformed/products_clean.csv"
)

engine = create_engine(
    "postgresql://airflow:airflow@postgres:5432/ecommerce_db"
)

df.to_sql(
    "products",
    engine,
    if_exists="replace",
    index=False
)

print("Load Complete")