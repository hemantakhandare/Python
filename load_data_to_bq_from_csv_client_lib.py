from google.cloud import bigquery
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\hemant\Desktop\python\rare-botany-344514-28d0a845d6c3.json"

from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "rare-botany-344514.mydataset1.emploadfromlfile"
file_path = r"C:\Users\hemant\Desktop\python\emp_data1.csv"

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE  #added to have truncate and insert load
)

with open(file_path, "rb") as source_file:
    job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    
job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
    )
)