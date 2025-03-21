# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose port
EXPOSE 8080

# Command to run the application
CMD ["gunicorn", "-c", "gunicorn-cfg.py", "config.wsgi"]

