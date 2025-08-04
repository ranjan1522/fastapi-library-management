from fastapi import APIRouter, HTTPException
from models import Member
from database import members_db
import logging

logging.basicConfig(level=logging.INFO)
router = APIRouter(prefix="/members")

@router.get("/")
def get_members():
    logging.info("👤 GET /members/ called")
    return [member.model_dump() for member in members_db]

@router.post("/")
def create_member(member: Member):
    if any(m.id == member.id for m in members_db):
        raise HTTPException(status_code=400, detail="Member with this ID already exists")
    members_db.append(member)
    return {"message": "Member added"}