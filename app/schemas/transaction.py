from pydantic import BaseModel, Field
from typing import Optional
import datetime

class TransactionCreate(BaseModel):
    amount: float = Field(..., gt=0)
    description: str

class TransactionUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0)
    description: Optional[str] = None
    status: Optional[str] = None

class TransactionResponse(BaseModel):
    id: int
    amount: float
    date: datetime.datetime
    description: str
    status: str

    class Config:
        orm_mode = True