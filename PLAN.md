# 🛫 Airfield Incident Management API — PLAN

---

# 📌 Project Overview

## 🎯 Goal
Build a production-style backend system that simulates how an AI-powered airport monitoring system processes object detection results and manages airfield incidents.

---

# 🧠 System Concept

Camera → AI Model → Backend API → Database → Incident Management

This project focuses on the backend part of the pipeline.

---

# 🏗 Final Deliverable

- FastAPI REST API
- PostgreSQL database
- SQLAlchemy ORM
- Alembic migrations
- Docker + docker-compose
- Unit tests (pytest)
- Logging
- AI integration (YOLO script)
- Clean architecture

---

# 🧱 Tech Stack

## Backend
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic

## Infrastructure
- Docker
- docker-compose

## Testing
- pytest

## AI Integration
- ultralytics (YOLOv8)
- requests

---

# 📂 Project Structure

app/
  main.py

  routers/
  services/
  repositories/
  models/
  schemas/
  core/

ai_simulator/
  detect_and_send.py

tests/
alembic/

Dockerfile
docker-compose.yml
requirements.txt
.env
PLAN.md
README.md

---

# 🧩 Core Entities

## Camera
- id
- location
- status

## Detection
- id
- camera_id (FK)
- object_type (debris, bird, vehicle)
- confidence_score
- timestamp

## Incident
- id
- detection_id (FK)
- status (OPEN, INVESTIGATING, RESOLVED)
- priority
- created_at
- resolved_at

## User
- id
- name
- role

---

# 🌐 API Endpoints

## Detections
POST /detections

## Incidents
GET /incidents  
GET /incidents/{id}  
PATCH /incidents/{id}/status  

## Users
POST /users  

## Cameras
GET /cameras  

---

# ⚙️ Business Logic

- A detection automatically creates an incident
- Incident lifecycle:
  OPEN → INVESTIGATING → RESOLVED
- Cannot resolve an already resolved incident
- Cannot skip states
- Validate all inputs

---

# 🤖 AI Integration

Script:
ai_simulator/detect_and_send.py

Steps:
1. Load pretrained YOLO model
2. Run detection on image
3. Extract object_type + confidence
4. Send POST requests to backend

---

# 🧠 Concepts to Learn

## Backend
- REST APIs
- HTTP lifecycle
- Status codes

## Architecture
- Layered structure
- Separation of concerns

## Database
- Relationships (FK, PK)
- Normalization
- Index basics

## ORM
- SQLAlchemy models
- Sessions
- Queries

## Migrations
- Alembic
- Schema versioning

## Docker
- Containers
- Networking
- Environment variables

## Testing
- Unit tests
- pytest basics

---

# 🗓 Roadmap

## Phase 1 — FastAPI Basics
- Setup app
- Basic routes

## Phase 2 — Database
- PostgreSQL
- SQLAlchemy models

## Phase 3 — Architecture
- routers / services / repositories

## Phase 4 — Alembic
- migrations

## Phase 5 — Business Logic
- incident lifecycle

## Phase 6 — AI Integration
- YOLO script

## Phase 7 — Testing
- pytest

## Phase 8 — Docker
- containerize app

## Phase 9 — Polish
- logging
- README

---

# 🧪 Testing

- Test service logic
- Test incident transitions
- Handle edge cases

---

# 🐳 Docker

- API container
- PostgreSQL container
- docker-compose setup

---

# 🚀 End Goal

A clean backend system that:
- Simulates AI integration
- Demonstrates backend engineering skills
- Can be explained clearly in interviews

---

# 🔥 Key Rule

Keep it:
- Clean
- Simple
- Well understood

NOT:
- Overengineered
