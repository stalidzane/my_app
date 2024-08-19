#!/bin/bash

# Check if Docker is installed; if not, install it
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Installing Docker..."
    sudo apt-get update
    sudo apt-get install -y docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    echo "Docker installed successfully."
else
    echo "Docker is already installed."
fi

# Build the Docker image for the Flask application
echo "Building Docker image..."
sudo docker build -t my-flask-app .

# Run the Docker container
echo "Running Docker container..."
sudo docker run -d -p 5000:5000 --name my-flask-container my-flask-app

# Check if the container is running
if docker ps | grep -q "my-flask-container"; then
    echo "Docker container 'my-flask-container' is running."
    echo "Access the Flask application at http://localhost:5000"
else
    echo "Failed to start Docker container."
    exit 1
fi