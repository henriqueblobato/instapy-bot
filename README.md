# 🐍 Python Application with Docker 🐳

This application is a simplistic Python-powered program, elegantly running within an efficient Docker container.

---

## 🚀 Docker Images

The Docker configuration starts with a minimalistic and lightweight base Docker image of `python:3.8.18-slim`. Additional libraries and tools are installed for a flawless runtime.

---

## ⚙️ Environment Setup

The Dockerfile sets up the following environment variables:

- `PYTHONDONTWRITEBYTECODE=1`: Disables writing of `.pyc` files.
- `PYTHONUNBUFFERED=1`: Forces the stdout and stderr streams to be unbuffered.

These provide an optimal environment for Python execution within the Docker container.

---

## 🌐 Firefox Setup Inside the Docker

The Docker image comes equipped with Firefox, ready to serve your browsing needs right out of the box!

---

## 👥 User Setup

The Docker configuration creates a new user named `appuser`, with minimalistic permissions for enhanced security. Required directories and permissions adjustments are neatly handled.

---

## 💼 Application Setup

The Dockerfile ensures all Python dependencies specified in `requirements.txt` are installed. Next, all application code is copied over into the Docker container.

---

## 🎉 Running the Application

To build and run the application, use the following command:
```shell
bash docker-compose up --build
```

Remember to replace `${INSTAGRAM_USERNAME}` and `${INSTAGRAM_PASSWORD_B64}` with your Instagram credentials.

🚀 The application should now be accessible at `localhost:8000`.

---
