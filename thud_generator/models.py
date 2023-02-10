from datetime import datetime

from pydantic import BaseModel, Field


class ThudSchema(BaseModel):
    id: int = Field(default=None)
    created_at: datetime.date

    class Config:
        schema_extra = {
            "example": {
                "id": 1234567890,
                "createdAt": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
        }
