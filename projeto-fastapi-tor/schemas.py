from pydantic import BaseModel

class AddIPInput(BaseModel):
    ip_address: str

class StandardOutput(BaseModel):
    message: str

class ErrorOutput(StandardOutput):
    detail: str

class IpListOutput(BaseModel):
    id: int
    ip_address: str

    class Config:
        orm_mode=True