# Start with a base Python 3.10 image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the working directory
COPY app.py .
COPY events.json .
COPY templates/ templates/

# Expose port 80
EXPOSE 80

# Start the FastAPI app
CMD ["uvicorn", "app:app", "--host=0.0.0.0", "--port=80"]
