# Waste Prediction Service

This project provides a gRPC-based service for waste prediction using a pre-trained machine learning model. The service can download the model from Kaggle, extract it, and use it to make predictions on waste images.

## Features

- **gRPC Service**: Provides a gRPC-based service for waste prediction.
- **Model Download and Extraction**: Downloads a pre-trained model from Kaggle and extracts it for use.
- **Docker Support**: Containerizes the application using Docker.
- **Configuration**: Uses environment variables for configuration.

## Setup

### Prerequisites

- Python 3.10
- Docker (optional, for containerization)

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/waste-prediction-service.git
   cd waste-prediction-service
   ```

2. Create and activate a virtual environment:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies

   ```sh
   pip install -r requirements.txt
   ```

4. Set up the environment variable in an .env file

   ```sh
   MODEL_ARCHIVE_PATH=your kaggle download url here
   ```

### Running the Application

1. Run the gRPC server

   ```python
   python app.py
   ```

### Docker Build

1. Build the Image

   ```sh
   docker build -t your_image_name .
   ```

2. Run the docker container

   ```sh
   docker run -e MODEL_ARCHIVE_PATH=your_kaggle_download_url \
             your_image_name
   ```
