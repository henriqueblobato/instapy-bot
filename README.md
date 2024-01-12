# Python Application with Docker

This application is a simple Python program running within a lightweight Docker container.

## Docker images

The base Docker image is `python:3.8.18-slim` and some additional libraries and tools are installed for necessary functioning.

## Environment Setup

The necessary environment variables are:

- **PYTHONDONTWRITEBYTECODE**: when set to any non-empty string, this prevents Python from writing `.pyc` files.
- **PYTHONUNBUFFERED**: when set to any non-empty string, this forces the stdout and stderr streams to be unbuffered.
  
Both variables are set to 1 in the Dockerfile.

## Firefox setup inside the Docker

Firefox is also installed in the Docker image and is available to use.

## User Setup

A new user named `appuser` is created with minimal permissions. All necessary directories and permissions are handled.

## Application Setup

Python dependencies are installed from `requirements.txt`. Then, the application code is copied over into the Docker container.

The application is then exposed on port 8000 and it's run via the command `python _runn.py`.

## Docker Compose

Through Docker Compose, the services are set up with necessary environmental variables from a .env file. The application is then run as well with the provided Instagram username and password.

## Building and Running the App
Make sure to replace the `${INSTAGRAM_USERNAME}` and `${INSTAGRAM_PASSWORD_B64}` with your actual Instagram credentials.

## Note
Ensure that the `requirements.txt` file is accurately populated with all the Python dependencies necessary for this application to run.