from sqlalchemy import Column, Integer, String, Boolean

from .database import db


class Ship(db.Model):
    __tablename__ = "ships"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    mass = Column(Integer, default=0)
    speed = Column(Integer, default=0)
    jump = Column(Integer, default=0)
    img_id = Column(String, nullable=True)
    deleted = Column(Boolean, nullable=False, default=False, server_default='false')