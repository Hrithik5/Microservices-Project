FROM python:3.10-slim-bullseye

# Install system dependencies including pkg-config
RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests \
  build-essential libpq-dev pkg-config \
  && pip install --no-cache-dir --upgrade pip

WORKDIR /app

# Copy and print requirements.txt for debugging
COPY ./requirements.txt /app
RUN cat /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --requirement /app/requirements.txt --verbose

# Copy the rest of the application code
COPY . /app

# Expose the application port
EXPOSE 8080

# Set the command to run the application
CMD ["python3", "server.py"]

