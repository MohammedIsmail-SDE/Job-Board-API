from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ── Auth Schemas ──────────────────────────────────────────────
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "candidate"  # "employer" or "candidate"


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    role: str
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


# ── Job Schemas ───────────────────────────────────────────────
class JobCreate(BaseModel):
    title: str
    description: str
    company: str
    location: str
    salary: Optional[str] = None
    job_type: str = "full-time"


class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    salary: Optional[str] = None
    job_type: Optional[str] = None
    is_active: Optional[bool] = None


class JobOut(BaseModel):
    id: int
    title: str
    description: str
    company: str
    location: str
    salary: Optional[str]
    job_type: str
    is_active: bool
    created_at: datetime
    employer_id: int

    class Config:
        from_attributes = True


# ── Application Schemas ───────────────────────────────────────
class ApplicationCreate(BaseModel):
    cover_letter: Optional[str] = None


class ApplicationOut(BaseModel):
    id: int
    cover_letter: Optional[str]
    status: str
    applied_at: datetime
    candidate_id: int
    job_id: int

    class Config:
        from_attributes = True


class ApplicationStatusUpdate(BaseModel):
    status: str  # "accepted" or "rejected"
