import logging
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    resource_id = req.route_params.get('id')
    
    try:
        req_body = req.get_json()
        resource_id = req.route_params.get('id')
        req_body['id'] = resource_id

        return func.HttpResponse(json.dumps(req_body), headers={"content-type": "application/json"})
    except ValueError:
        pass

    data = {
            'id': resource_id,
            'status': 'deleted'
            }

    return func.HttpResponse(json.dumps(data), headers={"content-type": "application/json"})
