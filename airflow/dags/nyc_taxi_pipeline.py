from datetime import timedelta

import pendulum
from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG

DATA_MONTH_TEMPLATE = (
    "{{ params.data_month if params.data_month else data_interval_start.strftime('%Y-%m') }}"
)

with DAG(
    dag_id="nyc_taxi_pipeline",
    schedule="0 6 5 * *",
    start_date=pendulum.datetime(
        2026,
        9,
        23,
        tz="UTC",
    ),
    catchup=False,
    max_active_runs=1,
    tags=["nyc-taxi"],
    params={
        "data_month": "",
    },
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=1),
    },
) as dag:
    download_raw_data = BashOperator(
        task_id="download_raw_data",
        bash_command="python src/download_raw_data.py",
        cwd="/opt/airflow/project",
        env={
            "DATA_MONTH": DATA_MONTH_TEMPLATE,
        },
        append_env=True,
    )

    load_raw_data = BashOperator(
        task_id="load_raw_data",
        bash_command="python src/load_raw_data.py",
        cwd="/opt/airflow/project",
        env={
            "DATA_MONTH": DATA_MONTH_TEMPLATE,
        },
        append_env=True,
    )

    dbt_build = BashOperator(
        task_id="dbt_build",
        bash_command=("dbt build --project-dir dbt --profiles-dir dbt"),
        cwd="/opt/airflow/project",
        env={
            "DATA_MONTH": DATA_MONTH_TEMPLATE,
        },
        append_env=True,
    )

    download_raw_data >> load_raw_data >> dbt_build
