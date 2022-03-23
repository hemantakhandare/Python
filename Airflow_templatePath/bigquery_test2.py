#step 1: Import required libraries.

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.operators.email_operator import EmailOperator
from airflow.utils.dates import days_ago, timedelta
from airflow.operators.dummy_operator import DummyOperator

#step 2: Set default argument variable.

"""Run a BQ query based on SQL."""
default_args = {"owner": "Hemant",
                "start_date": days_ago(2),
                "email": "hemantakhandare@gmail.com.com",
                "email_on_failure": True,
                "email_on_retry": True,
                "retries": 3,
                "retry_delay": timedelta(minutes=5)}

# Source
src_sql = """
insert into `rare-botany-344514.mydataset1.emp1` 
select 2,'insert from airflow',10;
"""


#step 3: initiate the DAG variable for all the task operators.

#gs://us-central1-airflowdemo-36e915ce-bucket/dags/scripts
#/home/airflow/gcs/dags/scripts
with DAG("bigquery_jinja_template",
         default_args=default_args,
         description="Run the sample Biqguery sql",
         schedule_interval=None,
         start_date=days_ago(2),
         catchup=False,
         template_searchpath="/home/airflow/gcs/dags/scripts" #This is the path where .sql files are placed and being refered using Jinja template
         
                  ) as dag:
       
                  
         #step 4:define the task action using the operator.
    
    #operators 1 defined
    
    """Run BQ Query sql using hardcoded text"""
    run_sql = BigQueryInsertJobOperator(
        task_id="run_sql1",
        configuration={"query": {"query": src_sql,
                                 "useLegacySql": False}},
        gcp_conn_id="my_gcp_connection"
    )
    
    
    """ run sqlfrom template_searchpath path """
    
    run_sql1 = BigQueryInsertJobOperator(
        task_id="run_sql_path",
        configuration={"query": {"query": "{% include 'testsql1.sql' %}",
                                 "useLegacySql": False}},
        gcp_conn_id="my_gcp_connection"
    )
   

    """ Dummy task """
    dummy_task = DummyOperator(task_id='DummyOperator')
    
    """ Dummy task """
    dummy_task1 = DummyOperator(task_id='DummyOperator1')

   #step 5:set dependency for the task
   
    run_sql>>dummy_task
    run_sql1>>dummy_task1 

