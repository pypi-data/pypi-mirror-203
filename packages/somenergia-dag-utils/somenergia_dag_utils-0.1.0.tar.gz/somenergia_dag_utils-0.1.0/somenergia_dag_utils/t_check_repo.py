from airflow.operators.python_operator import BranchPythonOperator
from airflow import DAG
import os.path

def repo_exists_check(repo_name):
    if os.path.exists(f'/opt/airflow/repos/{repo_name}/.git'):
        return 'git_pull_task'
    return 'git_clone'

def build_check_repo_task(dag: DAG, repo_name) -> BranchPythonOperator:
    check_repo_task = BranchPythonOperator(
        task_id='check_repo_task',
        python_callable=repo_exists_check,
        op_kwargs={ "repo_name": repo_name},
        do_xcom_push=False,
        dag=dag,
    )

    return check_repo_task
