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

# import logging

# import azure.functions as func


# def main(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )
