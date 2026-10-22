FROM python:3.9-slim

WORKDIR /app

# Install system packages, including libgl1 for OpenCV
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# Copy your application source code
COPY src/ ./src/
