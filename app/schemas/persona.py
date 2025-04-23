from pydantic import BaseModel

class PersonaCreate(BaseModel):
    educational_background: str
    family_background: str

class PersonaResponse(BaseModel):
    id: int
    educational_background: str
    family_background: str
    persona_text: str

class MessageResponse(BaseModel):
    message: str
    persona: PersonaResponse