import logging

import azure.functions as func
from PIL import Image
import io


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    logging.info("---------from-----------")
    res = "ssss"
    logging.info("-----------end---------")
    image_binary = ""
    if req.method == "POST":
        image_binary = req.get_body()
    img = Image.open(io.BytesIO(image_binary))
    grayscale_img = img.convert('L')
    png_binary = io.BytesIO()
    grayscale_img.save(png_binary, 'PNG')
    png_binary.seek(0)
    res = png_binary.getvalue()

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
