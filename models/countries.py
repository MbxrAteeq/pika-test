from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, JSON, Float


class Country(BaseModel):
    __tablename__ = "country"

    name = Column(String, unique=True)
    population = Column(Integer)
    area = Column(Float)
    data = Column(JSON)
