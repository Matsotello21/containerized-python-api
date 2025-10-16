# Containerized Python API

# Overview
This project is a simple, containerized REST API built with Python and Flask.
The API has a single endpoint that provides a basic health check, making it lightweight and straightforward example of a microservice.

# Technology Stack 
- Language: Python 
- Web Framework: Flask 
- Containerization: Docker 
- Version Control: Git & GitHub 

# Features 
- A simple Flask web server.
- A single REST API endpoint:
  * ``GET /status``: Returns a JSON object with the current status and version of the API
- A complete ``Dockerfile`` for building a production-ready container image 

# How to Run This Project Locally
To run this project, you will need to have Docker installed on your machine 

### Step 1: Clone the Repository 
First, clone this repository to your local machine 

``git clone [https://github.com/](https://github.com/)[Matsotello21]/containerized-python-api.git
cd containerized-python-api``

### Step 2: Build the Docker Image 
Navigate into the project directory and run the ``docker build`` command.This will create a Docker image based on the instructions in the ``Dockerfile``.

### Step 3: Run the Docker Container 
Once the image is built, you can run it as a container. This command maps port 5000 on your  local machine to port 5000 inside the container. 
``docker run -p 5000:5000 python-api-demo``

The API should now be running

### Step 4: Test the API Endpoint 
You can now test the ``/status`` endpoint by opening a new terminal and using ``curl``, or by visiting ``http://localhost:5000/status`` in your web browser.

``curl http://localhost:5000/status``

You should see the following JSON response:

```{
  "status": "ok",
  "version": "1.0.0"
}
```

