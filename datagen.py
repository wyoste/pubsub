import json
import csv
from google.cloud import pubsub_v1

project_name =  'nifty-matrix-463401-p3'
topic_name = 'sales'
file = 'Sales-1.csv'

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_name, topic_name)
print("Using topic path:", topic_path)
with open(file) as filehandle:
    rd = csv.DictReader(filehandle, delimiter=',')
    for row in rd:
        data_dict = {k: str(v) for k, v in row.items()}  # Ensure all values are strings
        data = json.dumps(data_dict)
        print(f"Publishing: {data}")
        publisher.publish(topic_path, data=data.encode('utf-8'))
