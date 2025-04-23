from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Persona(Base):
    __tablename__ = "personas"

    id = Column(Integer, primary_key=True, index=True)
    educational_background = Column(String, nullable=False)
    family_background = Column(String, nullable=False)
    persona_text = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint("educational_background", "family_background", name="uix_edu_family"),
    )