"""
Database Schemas for Portfolio contact messages

Model name is converted to lowercase for the collection name:
- ContactMessage -> "contactmessage" collection
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ContactMessage(BaseModel):
    name: str = Field(..., description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    message: str = Field(..., min_length=5, max_length=5000, description="Message body")
    source: Optional[str] = Field(None, description="Where the message was sent from (page, campaign, etc.)")
