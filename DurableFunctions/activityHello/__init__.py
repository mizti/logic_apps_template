# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
import os
import io
from azure.storage.blob import BlobServiceClient


def main(name: str) -> str:
    # TODO: Replace <storage-account-name> with your actual storage account name
    account_url = "https://targetfileio.blob.core.windows.net"
    shared_access_key = "jttTfDlh/pGri/K7lU57eA89+s8UkCMao7TbNmucOTZMFY9WL/empdOQqNMkiCCyu5UHYQWxbvLT+ASthRXRZw=="

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient(account_url, credential=shared_access_key)

    input_blob_client = blob_service_client.get_blob_client(container="input", blob="sample.txt")

    # readinto() downloads the blob contents to a stream and returns the number of bytes read
    stream = io.BytesIO()
    num_bytes = input_blob_client.download_blob().readinto(stream)
    logging.info(f"★Number of bytes: {num_bytes}")

    output_blob_client = blob_service_client.get_blob_client(container="output", blob="result.txt")
    input_stream = io.BytesIO(os.urandom(15))
    output_blob_client.upload_blob(input_stream, blob_type="BlockBlob")

    return f"Hello {name}!"
