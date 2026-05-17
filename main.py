from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from routers import auth, jobs, applications

# Create all tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Job Board API",
    description="A REST API for job postings and applications. Built with FastAPI + SQLAlchemy.",
    version="1.0.0",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(jobs.router)
app.include_router(applications.router)


@app.get("/", tags=["Health"])
def root():
    return {
        "message": "Welcome to Job Board API 🚀",
        "docs": "/docs",
        "redoc": "/redoc",
    }
