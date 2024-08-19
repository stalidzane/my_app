# Use an official Python image as the base
FROM python:3.12-slim
# Set the working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app.py"]
