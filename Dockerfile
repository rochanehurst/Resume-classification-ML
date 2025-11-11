# Use a lightweight official Python image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask runs on
EXPOSE 8080

# Set environment variable for Flask
ENV PORT=8080

# Start the Flask app
CMD ["python", "app.py"]
