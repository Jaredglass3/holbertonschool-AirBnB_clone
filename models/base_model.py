#!/usr/bin/env python3
"""Defines the BaseModel class."""
import models
from datetime import datetime
from os import getenv
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    """Defines the BaseModel class.
    Attributes:
        id (sqlalchemy String): The BaseModel id.
        created_at (sqlalchemy DateTime): The datetime at creation.
        updated_at (sqlalchemy DateTime): The datetime of last update.
    """

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
