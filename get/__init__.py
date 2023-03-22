import logging
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a get request.')

    data = get_resource()
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})

def get_resource():
# Implement CosmosDB get resource here
    data = {
        'resources':[
        {
            'id': '0',
            'name': 'Resource 0',
            'description': 'This is resource 0',
            'status': 'available'
        },
        {
            'id': '1',
            'name': 'Resource 1',
            'description': 'This is resource 1',
            'status': 'available'
        }
        ]}
    return data
