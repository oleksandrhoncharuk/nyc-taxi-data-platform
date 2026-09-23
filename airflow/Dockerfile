FROM apache/airflow:3.3.1-python3.13

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir \
    pandas \
    pyarrow \
    sqlalchemy \
    "psycopg[binary]" \
    python-dotenv \
    dbt-postgres
