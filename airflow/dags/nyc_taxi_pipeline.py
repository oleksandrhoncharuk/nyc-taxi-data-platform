from airflow.sdk import DAG
from datetime import timedelta
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="nyc_taxi_pipeline",
    schedule=None,
    catchup=False,
    tags=["nyc-taxi"],
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=1),
    },
) as dag:

    download_raw_data = BashOperator(
        task_id="download_raw_data",
        bash_command="python src/download_raw_data.py",
        cwd="/opt/airflow/project",
    )

    load_raw_data = BashOperator(
        task_id="load_raw_data",
        bash_command="python src/load_raw_data.py",
        cwd="/opt/airflow/project",
    )

    dbt_build = BashOperator(
        task_id="dbt_build",
        bash_command=(
            "dbt build "
            "--project-dir dbt "
            "--profiles-dir dbt"
        ),
        cwd="/opt/airflow/project",
    )

    download_raw_data >> load_raw_data >> dbt_build
