# Use the official Python 3.12 image as the base image
FROM python:3.12

# Update package lists, install CMake, build tools, and AWS CLI
RUN apt update -y && apt install -y \
    build-essential \
    cmake \
    awscli \
    curl \
    unzip

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements.txt first to leverage Docker's cache
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app

# Command to run the Python application
CMD ["python3", "app.py"]