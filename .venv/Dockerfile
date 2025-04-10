# Start with Python image
FROM python:3.11-slim

# This avoids extra files and helps with debugging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the folder inside the container
WORKDIR /app

# Put everything into the container
COPY . .

# Install what's needed
RUN pip install --no-cache-dir -r requirements.txt

# Open up the port
EXPOSE 5001

# Run the Python file
CMD ["python", "watson_tts_server.py"]
