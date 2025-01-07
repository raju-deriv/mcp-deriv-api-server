# Use Python 3.11 as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install pip and project dependencies
RUN pip install --no-cache-dir pip --upgrade

# Copy project files
COPY pyproject.toml .
COPY server.py .
COPY services/ services/

# Install project dependencies
RUN pip install --no-cache-dir .

# Copy .env file if it exists (for development)
COPY .env* ./

# Expose any necessary ports (if needed)
# EXPOSE 8000

# Run the server
CMD ["python", "server.py"]
