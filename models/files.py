from typing import Optional
from pydantic import BaseModel
'''
The class Files is a subclass of BaseModel. It has three attributes: id, name, and data. The id attribute is optional, and the name and data attributes are required. The id attribute is a string, and the name and data attributes are bytes
'''
class Files(BaseModel):
    id: Optional[str]
    name: str
    data: bytes