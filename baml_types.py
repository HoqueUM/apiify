import pydantic
from typing import List

class Attribute(pydantic.BaseModel):
    name: str
    value: str
class Metadata(pydantic.BaseModel):
    part: str
    tag: str
    content: str
    attributes: List[Attribute]