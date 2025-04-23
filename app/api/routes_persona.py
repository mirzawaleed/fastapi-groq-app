from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.persona import PersonaCreate, MessageResponse
from app.models.persona import Persona
from app.db.session import get_db
from app.services.groq import generate_persona_text
from fastapi import Query
from typing import List
from app.schemas.persona import PersonaResponse

router = APIRouter(prefix="/personas", tags=["Personas"])

@router.post("/generate", response_model=MessageResponse, status_code=201)
async def generate_and_store_persona(data: PersonaCreate, db: Session = Depends(get_db)):
    existing = db.query(Persona).filter_by(
        educational_background=data.educational_background.strip(),
        family_background=data.family_background.strip()
    ).first()

    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with this educational and family background already exists"
        )

    try:
        persona_text = await generate_persona_text(
            data.educational_background,
            data.family_background
        )
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

    persona = Persona(
        educational_background=data.educational_background.strip(),
        family_background=data.family_background.strip(),
        persona_text=persona_text
    )
    db.add(persona)
    db.commit()
    db.refresh(persona)

    return {"message": "User persona generated and stored successfully", "persona": persona}

# Endpoint: Search user personas
@router.get("/search", response_model=List[PersonaResponse], status_code=200)
def search_personas(q: str = Query(..., min_length=1), db: Session = Depends(get_db)):
    try:
        results = db.query(Persona).filter(
            Persona.persona_text.ilike(f"%{q}%")
        ).all()
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")

