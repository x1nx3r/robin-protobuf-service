import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    MODEL_ARCHIVE_PATH = os.getenv('MODEL_ARCHIVE_PATH')
    EXTRACTED_MODEL_DIR = os.path.join(os.getcwd(), 'model_dir')
    KAGGLE_USERNAME = os.getenv('KAGGLE_USERNAME')
    KAGGLE_KEY = os.getenv('KAGGLE_KEY')