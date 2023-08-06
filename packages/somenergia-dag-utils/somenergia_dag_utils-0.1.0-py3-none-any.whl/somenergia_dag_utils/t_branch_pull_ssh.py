from airflow.operators.python_operator import BranchPythonOperator
from airflow import DAG
import paramiko
import io

from random import randint
from time import sleep

class GitPullError(Exception): pass

def pull_repo_ssh(repo_name, repo_server_url, repo_server_key, task_name, dag_id=None):
    p = paramiko.SSHClient()
    p.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    keyfile = io.StringIO(repo_server_key)
    mykey = paramiko.RSAKey.from_private_key(keyfile)
    p.connect(repo_server_url, port=2200, username="airflow", pkey=mykey)

    # randomly wait to prevent locks
    # TODO should use a dedicated DAG for all alerts
    sleep(randint(1,10))

    stdin, stdout, stderr = p.exec_command(f"git -C /opt/airflow/repos/{repo_name} fetch")
    txt_stderr = stderr.readlines()

    # TODO might be too fragile
    if txt_stderr and not (txt_stderr[0].startswith('remote') or txt_stderr[0].startswith('From') or txt_stderr[0].startswith('Warning')):
        print (f"Stderr of git fetch returned {txt_stderr} and {stdout.readlines()}.")
        raise GitPullError(txt_stderr)
    else:
        print (f"git fetch returned {txt_stderr} and {stdout.readlines()}.")

    stdin, stdout, stderr = p.exec_command(f"git -C /opt/airflow/repos/{repo_name} diff origin/main -- requirements.txt")
    txt_stdout = stdout.readlines()
    txt_stdout = "".join(txt_stdout)
    requirements_updated = len(txt_stdout) > 0
    if txt_stderr and not (txt_stderr[0].startswith('remote') or txt_stderr[0].startswith('From')):
        print (f"Stderr of git diff requirements returned {txt_stderr}. {bool(txt_stderr)}")
        raise GitPullError(txt_stderr)
    if requirements_updated:
        print (f"Stdout de git diff requirements retornat {txt_stdout} and needs update")
    else:
        print (f"Stdout de git diff requirements no ha retornat cap missatge {txt_stdout}. stdout {stdout.readlines()}")
    stdin, stdout, stderr = p.exec_command(f"git -C /opt/airflow/repos/{repo_name} pull")
    txt_stderr = stderr.readlines()
    txt_stderr = "".join(txt_stderr)
    print (f"Stderr de git pull ha retornat {txt_stderr}")
    # si stderr té més de 0 \n és que hi ha canvis al fer pull
    #Your configuration specifies to merge with the ref 'refs/heads/main' from the remote, but no such ref was fetched.
    #Apareix quan fem molts git pull a la vegada

    # image removal and build is not working atm
    print(f'dag id is {dag_id}')
    if dag_id and dag_id == 'dades_sandbox_dag':
        print(f"Requirements updated? {requirements_updated}")
        return 'update_docker_image' if requirements_updated else task_name
    else:
        return task_name

def build_branch_pull_ssh_task(dag: DAG, task_name, repo_name) -> BranchPythonOperator:
    branch_pull_ssh_task = BranchPythonOperator(
        task_id='git_pull_task',
        python_callable=pull_repo_ssh,
        op_kwargs={ "repo_name": repo_name,
                    "repo_server_url": "{{ var.value.repo_server_url }}",
                    "repo_server_key": "{{ var.value.repo_server_key }}",
                    "task_name": task_name,
                    "dag_id": dag.dag_id},
        do_xcom_push=False,
        dag=dag
    )

    return branch_pull_ssh_task
