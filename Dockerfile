# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install grpcio-tools for generating gRPC files
RUN pip install grpcio-tools

# Copy the current directory contents into the container at /app
COPY . .

# Generate gRPC files with relative imports
RUN python -m grpc_tools.protoc -I=protos --python_out=. --grpc_python_out=. protos/waste_prediction.proto

# Run the invoke_model_utils.py script to download and extract the model
RUN python invoke_model_utils.py

# Run the application
CMD ["python", "app.py"]