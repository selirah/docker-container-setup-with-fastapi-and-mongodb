# 🚀 FastAPI + MongoDB (Docker)

A lightweight backend powered by **FastAPI**, **Beanie/Motor**, and **MongoDB**, fully containerized with **Docker Compose**.  
This README explains how to configure, run, and extend the stack.

---

---

### 🔧 Requirements

- Docker & Docker Compose  
- (Optional) Python 3.11+ for local development  
- A `.env` file providing your MongoDB connection string

---

### ⚙️ Environment Variables

Create a `.env` file in the project root:

```env
# .env
MONGODB_URI=mongodb://mongo:27017/mydb

If running the backend without Docker:
MONGODB_URI=mongodb://localhost:27017/mydb
```

### 🐳 Running with Docker

Start all services
```
docker compose up --build
```

Run detached
```
docker compose up -d
```

Stop containers
```
docker compose down
```

Remove containers + volumes
```
docker compose down -v
```

### 🌐 Accessing the API

Once running:
* Health check → http://localhost:8000/
* Swagger UI → http://localhost:8000/docs


### 🗄️ MongoDB Access
Host machine:
```
mongodb://localhost:27017
```

Inside Docker network (used by your FastAPI app):
```
mongodb://mongo:27017/mydb
```

### 🧩 Available API Endpoints
**GET /**
* Returns a simple health message.

**GET /me**
* Fetch current user information.

**PUT /me**
* Update the authenticated user.

All endpoints are documented automatically at /docs.