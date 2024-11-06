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

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY proj-dj .

# Expose the port the app will run on
EXPOSE 8000

# Run the Django development server (adjust for production if needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]