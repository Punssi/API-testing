import logging
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a get request.')

    req_body = req.get_json()
    resource_id = req.route_params.get('id')

    req_body['id'] = resource_id
    
    # data = {
    #         'id': resource_id,
    #         'name': f'Resource {resource_id}',
    #         'status': 'uppdated'
    #         }

    return func.HttpResponse(json.dumps(req_body), headers={"content-type": "application/json"})
