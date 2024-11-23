# Use an official Python runtime as a parent image
FROM python:3.1-slim

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

# Generate gRPC files
RUN python -m grpc_tools.protoc -I=protos --python_out=src/generated --grpc_python_out=src/generated protos/waste_prediction.proto

# Set environment variables (if needed)
ENV MODEL_ARCHIVE_PATH=bahiskaraananda/robin-efficientnetv2s/tensorFlow2/1.0-18m-ft144
ENV KAGGLE_USERNAME=meganugraha
ENV KAGGLE_KEY=c2ee120b5792464fdf5468c81c913dd1

# Run the application
CMD ["python", "src/grpc_server.py"]