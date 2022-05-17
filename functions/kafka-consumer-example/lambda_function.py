import json
import base64

def lambda_handler(event, context):
    print(f"Event: {event}")
    for key in event['records']:
        print(f"Key: {key}")
        for record in event['records'][key]:
            print(f"Record: {record}")
            message = base64.b64decode(record['value']).decode('utf-8')
            print(f"Message: {message}")
            
