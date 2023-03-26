from pydantic import BaseModel

# parameter schema
class Data(BaseModel):
    url: str