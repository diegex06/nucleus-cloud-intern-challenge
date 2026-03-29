\# Cloud Intern Challenge – Hello + System Info Web Service



\## Overview



This project is a containerized web application that demonstrates a simple cloud-style architecture using Docker Compose.



It includes:

\- A Flask API that returns system and request metadata

\- An Nginx reverse proxy handling HTTPS traffic

\- Self-signed TLS certificates generated at runtime

\- Multi-container orchestration using Docker Compose



\---



\## Architecture



The request flow is:



Client (Browser)

→ HTTPS (port 443)

→ Nginx Reverse Proxy

→ Flask Application (internal Docker network)



Nginx handles TLS termination and forwards requests to the Flask backend.



\---



\## Features



\- Returns JSON response with:

&#x20; - Greeting message

&#x20; - Hostname (container ID)

&#x20; - Current UTC timestamp

&#x20; - Client IP address

&#x20; - Full request headers



\- HTTPS enabled via self-signed certificate

\- Reverse proxy using Nginx

\- Containerized deployment using Docker Compose



\---



\## Project Structure

cloud-intern-challenge/

│

├── app/

│ └── app.py # Flask application

│

├── nginx/

│ └── nginx.conf # Nginx reverse proxy config

│

├── Dockerfile # Flask container build instructions

├── docker-compose.yml # Multi-container orchestration

├── .gitignore

└── README.md

---



\## How to Run



\### 1. Clone the repository

```bash

git clone https://github.com/YOUR\_USERNAME/cloud-intern-challenge.git

cd cloud-intern-challenge

### 2. Start the application
docker compose up --build

### 3. Open in browser

https://localhost

---



\## Notes



\- Uses a self-signed SSL certificate generated at runtime

\- All services run inside isolated Docker containers



