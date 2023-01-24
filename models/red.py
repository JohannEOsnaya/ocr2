from typing import Optional
from pydantic import BaseModel

class Red(BaseModel):
    id: Optional[str]
    citas: list[str]