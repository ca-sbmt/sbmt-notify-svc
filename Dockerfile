# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the pyproject.toml file
COPY pyproject.toml .

# Install any needed packages specified in pyproject.toml
RUN pip install --no-cache-dir --trusted-host pypi.python.org poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copy the rest of the application code
COPY . .

# Expose the required port for the application
EXPOSE 8000

# Set the environment variable for the environment type
ENV ENV_TYPE=dev

# Define the command to run the application using run.py
CMD ["python", "run.py"]
