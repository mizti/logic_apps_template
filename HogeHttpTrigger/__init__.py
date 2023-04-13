import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info("---------from-----------")    
    res = "ssss"
    logging.info("-----------end---------")
    if req.method == "POST":
        res = req.get_body()

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             body = res,
             status_code=200,
             mimetype = "image"
        )
        #return func.HttpResponse(
        #     body = res,
        #     status_code=200,
        #     mimetype = "image/png"
        #)
