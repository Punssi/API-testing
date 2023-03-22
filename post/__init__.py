import logging
import json
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a get request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass

    return func.HttpResponse(json.dumps(req_body))
