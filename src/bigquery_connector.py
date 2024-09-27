from google.cloud import bigquery

def connect_bigquery():
    """Connect to the BigQuery client."""
    client = bigquery.Client()
    return client

def run_query(client, query):
    """Run a SQL query on BigQuery."""
    query_job = client.query(query)
    results = query_job.result()  # Wait for the query to finish
    return results.to_dataframe()

def load_data_to_bigquery(client, data, table_id):
    """Load a DataFrame into BigQuery."""
    job = client.load_table_from_dataframe(data, table_id)
    job.result()  # Wait for the job to complete
    print(f"Loaded {len(data)} rows to {table_id}")

