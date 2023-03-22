import logging
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a get request.')

    try:
        resource_id = req.route_params.get('id')
    except ValueError:
        pass
    
    try:
        data = get_one_resource(resource_id)
    except ValueError:
        pass
    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})

def get_one_resource(resource_id):

   #Implement CosmosDB get resource here
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
    return data['resources'][int(resource_id)]
