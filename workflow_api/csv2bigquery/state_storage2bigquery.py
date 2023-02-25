from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

table_id = "artful-turbine-378406.pizza_delivery.state_population"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("population", "INTEGER"),
    ],
    skip_leading_rows=0, # skip "header rows"!
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
uri = "gs://artful-turbine-378406/state_population.csv"

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)  # Make an API request.
print("Loaded {} rows.".format(destination_table.num_rows))
