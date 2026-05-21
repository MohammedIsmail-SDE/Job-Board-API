from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models, schemas
from auth_utils import get_current_user, require_employer

router = APIRouter(prefix="/applications", tags=["Applications"])


@router.post("/job/{job_id}", response_model=schemas.ApplicationOut, status_code=201)
def apply_to_job(job_id: int, data: schemas.ApplicationCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    if current_user.role != "candidate":
        raise HTTPException(status_code=403, detail="Only candidates can apply")
    job = db.query(models.Job).filter(models.Job.id == job_id, models.Job.is_active == True).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    already = db.query(models.Application).filter(
        models.Application.candidate_id == current_user.id,
        models.Application.job_id == job_id
    ).first()
    if already:
        raise HTTPException(status_code=400, detail="Already applied")
    application = models.Application(cover_letter=data.cover_letter, candidate_id=current_user.id, job_id=job_id)
    db.add(application)
    db.commit()
    db.refresh(application)
    
  
    return application


@router.get("/my", response_model=List[schemas.ApplicationOut])
def my_applications(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(models.Application).filter(models.Application.candidate_id == current_user.id).all()


@router.get("/job/{job_id}", response_model=List[schemas.ApplicationOut])
def applications_for_job(job_id: int, db: Session = Depends(get_db), current_user=Depends(require_employer)):
    job = db.query(models.Job).filter(models.Job.id == job_id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    if job.employer_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return db.query(models.Application).filter(models.Application.job_id == job_id).all()


@router.patch("/{application_id}/status", response_model=schemas.ApplicationOut)
def update_status(application_id: int, data: schemas.ApplicationStatusUpdate, db: Session = Depends(get_db), current_user=Depends(require_employer)):
    if data.status not in ["accepted", "rejected"]:
        raise HTTPException(status_code=400, detail="Status must be 'accepted' or 'rejected'")
    application = db.query(models.Application).filter(models.Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    if application.job.employer_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    application.status = data.status

    db.refresh(application)
    return application