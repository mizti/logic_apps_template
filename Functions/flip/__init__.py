import logging

import azure.functions as func
from PIL import Image
import io

def main(req: func.HttpRequest) -> func.HttpResponse:
    image_binary = ""
    if req.method == "POST":
        image_binary = req.get_body()
    img = Image.open(io.BytesIO(image_binary))

    # Process image here
    processed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

    # Save image
    png_binary = io.BytesIO()
    processed_img.save(png_binary, 'PNG')
    png_binary.seek(0)
    response = png_binary.getvalue()

    return func.HttpResponse(
            body = response,
            status_code=200,
            mimetype = "image"
    )