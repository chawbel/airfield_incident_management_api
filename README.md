# Airfield Incident Management API

![CI/CD](https://github.com/chawbel/airfield_incident_management_api/actions/workflows/ci.yml/badge.svg)

## Overview
Airfield Incident Management API is a simulation system designed to automate incident dispatching on airfields using AI-powered camera feeds. It listens for real-time detections (like birds, vehicles, or debris) from a simulated YOLOv8 AI model, processes them, and automatically generates tracking incidents for airfield security personnel.

This project was built to demonstrate a modern, production-ready backend architecture using FastAPI, SQLAlchemy 2.0, PostgreSQL, Docker, and GitHub Actions for CI/CD.

## Architecture

The application follows a **Clean Architecture** pattern, ensuring a strong separation of concerns between web routing, business logic, and database access:

```mermaid
graph TD;
    Client[AI Simulator / YOLOv8] -->|HTTP POST| Router[FastAPI Routers];
    
    subgraph Core API
    Router --> Service[Business Logic / Services];
    Service --> Repository[Data Access / Repositories];
    end
    
    Repository --> DB[(PostgreSQL Database)];
```

### Components:
- **Routers (`app/routers/`)**: Handles incoming HTTP requests and validates payloads using Pydantic schemas.
- **Services (`app/services/`)**: Contains the core business logic (e.g., rules for transitioning incident states).
- **Repositories (`app/repositories/`)**: Manages all database interactions, keeping SQL queries isolated from business logic.
- **Models (`app/models/`)**: SQLAlchemy ORM models defining the database schema.
- **AI Simulator (`ai_simualtor/`)**: A standalone Python script that uses a pre-trained YOLOv8 neural network to detect objects in images and send them to the API.

## Features
- **Real-time AI Integration**: Accepts detections from a YOLOv8 computer vision model.
- **Automated Incident Creation**: Automatically creates tracked incidents when specific hazards (birds, vehicles, debris) are detected on the airfield.
- **State Management**: Enforces valid state transitions for incidents (e.g., `OPEN` -> `INVESTIGATING` -> `RESOLVED`).
- **Robust Error Handling**: Centralized business exception handling returning consistent, predictable API errors.
- **Observability**: Built-in request tracing and centralized logging.
- **CI/CD Pipeline**: Fully automated testing and Docker image publishing to GitHub Container Registry (GHCR) via GitHub Actions.

## Technologies Used
- **Backend Framework**: FastAPI, Pydantic
- **Database & ORM**: PostgreSQL, SQLAlchemy 2.0, Alembic
- **AI / Computer Vision**: Ultralytics (YOLOv8)
- **Testing**: Pytest
- **Containerization**: Docker, Docker Compose
- **CI/CD**: GitHub Actions, GitHub Container Registry (GHCR)

## Getting Started

### Prerequisites
- Docker and Docker Compose installed on your machine.
- Git.

### Running with Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/chawbel/airfield_incident_management_api.git
   cd airfield_incident_management_api
   ```

2. **Start the application:**
   ```bash
   docker-compose up --build
   ```
   This will spin up both the PostgreSQL database and the FastAPI application. Alembic migrations will automatically run to set up your database schema.

3. **Access the API Documentation:**
   Open your browser and navigate to `http://localhost:8000/docs` to interact with the auto-generated Swagger UI.

### Running the AI Simulator

The project includes a simulator that processes sample images using a YOLOv8 model and sends the detections to the API.

1. **Enter the simulator directory:**
   ```bash
   cd ai_simualtor
   ```

2. **Run the simulator:**
   *(Note: The simulator script is configured to point to `http://api:8000/detection/` for Docker networking. If running locally outside Docker, change the `API_URL` to `http://127.0.0.1:8000/detection/` in `detect_and_send.py`.)*
   ```bash
   # Install dependencies if running locally
   pip install ultralytics requests
   
   python detect_and_send.py
   ```

## Running Tests
Tests are executed automatically in the CI pipeline using a lightweight SQLite database. To run them locally:

```bash
DATABASE_URL="sqlite:///./test_local.db" pytest tests/ -v
```

## Pulling the Pre-built Docker Image
You can pull the latest built image directly from the GitHub Container Registry without needing the source code:

```bash
docker pull ghcr.io/chawbel/airfield_incident_management_api:latest
```
To run the image standalone (requires a separate Postgres database):
```bash
docker run -p 8000:8000 -e DATABASE_URL="postgresql://user:password@host:5432/db" ghcr.io/chawbel/airfield_incident_management_api:latest
```

## License
MIT License
