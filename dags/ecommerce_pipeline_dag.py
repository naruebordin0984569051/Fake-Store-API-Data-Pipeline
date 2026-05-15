from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="ecommerce_pipeline",
    start_date=datetime(2025,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    extract_task = BashOperator(
        task_id="extract_products",
        bash_command="python /opt/airflow/scripts/extract.py"
    )

    transform_task = BashOperator(
        task_id="transform_products",
        bash_command="python /opt/airflow/scripts/transform.py"
    )

    load_task = BashOperator(
        task_id="load_products",
        bash_command="python /opt/airflow/scripts/load.py"
    )

    extract_task >> transform_task >> load_task