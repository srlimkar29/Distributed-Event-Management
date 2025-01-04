# Use a Python base image
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the service port
EXPOSE 3003

# Start the service
CMD ["python", "app.py"]
