from airflow import DAG
from airflow.operators.python import PythonOperator  # Correct import for PythonOperator in Airflow 2.10.2
from airflow.utils.dates import days_ago
from crawl.main import main  # Import the main function

# Define the default arguments for the DAG
default_args = {
    'owner': 'PhiNguyen',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'crawl_dag',
    default_args=default_args,
    description='Crawl data from tiki and load into sqlite',
    schedule_interval=None,
    start_date=days_ago(1),
    catchup=False,
)

# Define the PythonOperator
run_crawl_task = PythonOperator(
    task_id='run_main_function',
    python_callable=main,
    dag=dag,
)

# Set the task in the DAG
run_crawl_task