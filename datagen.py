import json
import csv
from google.cloud import pubsub_v1

project_name =  'yoste123'
topic_name = 'sales'
file = 'sales.csv'

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_name, topic_name)
print("Running Datagen.py!") 
print("Using topic path:", topic_path)
with open(file) as filehandle:
    rd = csv.DictReader(filehandle, delimiter=',')
    for row in rd:
        data = json.dumps(dict(row))
        print(f"Publishing: {data}")
        publisher.publish(topic_path, data=data.encode('utf-8'))
        print("**published**")
