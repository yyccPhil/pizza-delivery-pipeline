from google.cloud import bigquery
import os
from google.api_core.exceptions import BadRequest
# import json


def format_schema(schema):
    formatted_schema = []
    for row in schema:
        formatted_schema.append(bigquery.SchemaField(row['name'], row['type'], row['mode']))
    return formatted_schema


credentials_path = "pizza_delivery_privatekey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

job_config = bigquery.QueryJobConfig(dry_run=False, use_query_cache=True)

table_schema = {
    'name': 'order_id',
    'type': 'INTEGER',
    'mode': 'REQUIRED'
    },{
        'name': 'customer_id',
        'type': 'INTEGER',
        'mode': 'NULLABLE'
    },{
        'name': 'pizza_type',
        'type': 'STRING',
        'mode': 'NULLABLE'
    },{
        'name': 'qty',
        'type': 'INTEGER',
        'mode': 'NULLABLE'
    },{
        'name': 'retail_price',
        'type': 'FLOAT',
        'mode': 'NULLABLE'
    },{
        'name': 'order_date',
        'type': 'DATETIME',
        'mode': 'NULLABLE'
    }


project_id = 'artful-turbine-378406'
dataset_id = 'pizza_delivery'
table_id = 'orders'

client  = bigquery.Client(project = project_id)
dataset  = client.dataset(dataset_id)
table = dataset.table(table_id)

job_config = bigquery.LoadJobConfig()
job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
job_config.schema = format_schema(table_schema)


with open('orders_yesterday.json', 'rb') as source_file:
    job = client.load_table_from_file(
        source_file,
        table,
        job_config=job_config
    )
    try:
        print(job.result())
    except BadRequest as e:
        for e in job.errors:
            print('ERROR: {}'.format(e['message']))