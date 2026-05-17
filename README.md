# 🚀 Job Board API

A production-ready REST API built with **FastAPI** and **SQLAlchemy** for job postings and applications.

## ⚙️ Tech Stack
- **FastAPI** — Modern, fast Python web framework
- **SQLAlchemy** — ORM for database management
- **SQLite** — Lightweight database (swap to PostgreSQL for production)
- **JWT** — Secure authentication
- **Pydantic** — Data validation

## 📦 Setup & Run

```bash
# 1. Clone the repo
git clone https://github.com/yourusername/job-board-api.git
cd job-board-api

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
uvicorn main:app --reload
```

Open **http://localhost:8000/docs** to explore the API with Swagger UI.

## 🔑 API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register as employer or candidate |
| POST | `/auth/login` | Login and get JWT token |

### Jobs
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/jobs/` | List all jobs (with search/filter) |
| GET | `/jobs/{id}` | Get job details |
| POST | `/jobs/` | Post a new job *(employer only)* |
| PUT | `/jobs/{id}` | Update a job *(employer only)* |
| DELETE | `/jobs/{id}` | Delete a job *(employer only)* |

### Applications
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/applications/job/{job_id}` | Apply to a job *(candidate only)* |
| GET | `/applications/my` | View my applications *(candidate)* |
| GET | `/applications/job/{job_id}` | View applicants *(employer only)* |
| PATCH | `/applications/{id}/status` | Accept/reject application *(employer)* |

## 🔐 Authentication
This API uses **JWT Bearer Tokens**. After login, include the token in the header:
```
Authorization: Bearer <your_token>
```

## 🗂️ Project Structure
```
job-board-api/
├── main.py           # App entry point
├── database.py       # DB connection & session
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic schemas
├── auth_utils.py     # JWT & password utilities
├── routers/
│   ├── auth.py       # Register & Login
│   ├── jobs.py       # Job CRUD
│   └── applications.py # Apply & manage
└── requirements.txt
```

## 🚀 Deploy to Render (Free)
1. Push code to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your repo
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Deploy!
