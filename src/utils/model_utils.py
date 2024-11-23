import os
import shutil
import requests
import tarfile
from config import Config

def download_and_extract_model():
    # Define the URL for the model download
    model_url = f"{Config.MODEL_ARCHIVE_PATH}"

    # Define the path to save the downloaded archive
    archive_copy_path = os.path.join(Config.EXTRACTED_MODEL_DIR, 'model_archive.tar.gz')

    # Ensure the destination directory exists
    os.makedirs(Config.EXTRACTED_MODEL_DIR, exist_ok=True)

    # Download the model using requests
    with requests.get(model_url, stream=True) as r:
        r.raise_for_status()
        with open(archive_copy_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"Downloaded model to: {archive_copy_path}")

    # Extract the archive
    with tarfile.open(archive_copy_path, 'r:gz') as tar:
        tar.extractall(Config.EXTRACTED_MODEL_DIR)

    print("Model downloaded and extracted to:", Config.EXTRACTED_MODEL_DIR)