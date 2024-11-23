# Robin protobuf-gRPC Service

A gRPC-based service for our waste prediction model, Robin. The service downloads the model from Kaggle, extracts it, and uses it to make predictions on waste images.

This service is designed to run as a subsidiary for our backend app in Google Cloud Run, enabling a high-performance microservice architecture.

## Project Structure

```plain
project_root/
│
├── protos/
│   └── waste_prediction.proto
│
├── src/
│   ├── utils/
│   │   └── model_utils.py
│   └── grpc_handler.py
│
├── .env
├── config.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── app.py
├── waste_prediction_pb2.py
└── waste_prediction_pb2_grpc.py
```

## Features

- **gRPC Service**: Provides a gRPC-based service for waste prediction.
- **Model Download and Extraction**: Downloads a pre-trained model from Kaggle and extracts it for use.
- **Docker Support**: Containerizes the application using Docker.
- **Configuration**: Uses environment variables for configuration.

## Setup

### Prerequisites

- Python 3.10
- Docker (optional, for containerization)

### Installation on Local Machine (without Docker)

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
   MODEL_ARCHIVE_PATH=your_kaggle_download_url_here
   ```

5. Generate gRPC config

   ```sh
   python -m grpc_tools.protoc -I=protos --python_out=. --grpc_python_out=. protos/waste_prediction.proto
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
