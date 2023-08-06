import os.path

from airflow import DAG
from airflow.operators.python_operator import BranchPythonOperator

# TODO finish this


def get_server_environment():
    if os.path.exists("/opt/airflow/repos/.env.prod"):
        return "is_prod"
    return "is_pre"


def build_check_repo_task(dag: DAG) -> BranchPythonOperator:
    check_repo_task = BranchPythonOperator(
        task_id="check_repo_task",
        python_callable=get_server_environment,
        do_xcom_push=False,
        dag=dag,
    )

    return check_repo_task
