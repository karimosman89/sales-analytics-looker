from google.cloud import bigquery
import pandas as pd

def load_sales_data_to_bigquery(csv_file, table_id):
    client = bigquery.Client()
    data = pd.read_csv(csv_file)

    job = client.load_table_from_dataframe(data, table_id)
    job.result()  # Wait for the job to complete
    print(f"Loaded {data.shape[0]} rows to {table_id}")

