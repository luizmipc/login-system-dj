# Use the official Python image from the Docker Hub
FROM python:3.12.4

# Set the working directory in the container
WORKDIR /proj-dj

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file from login-system-dj directory
COPY proj-dj/requirements.txt .
COPY proj-dj .
COPY entrypoint.sh /entrypoint.sh

EXPOSE 8000

# Install Python dependencies
RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /proj-dj/requirements.txt && \
    chmod +x /entrypoint.sh
# Copy the entire project directory into the containe
ENV PATH="/scripts:/venv/bin:$PATH"

# Expose the port the app will run on
# Run the Django development server (adjust for production if needed)
ENTRYPOINT [ "/entrypoint.sh" ]