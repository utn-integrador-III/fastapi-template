
from pydantic import BaseModel, Field
from models.Student.Priority import Priority

class StudentBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="The name of the student")
    age: int  = Field(..., gt=0, le=120, description="The age of the student")
    year: str = Field(..., min_length=2, max_length=50, description="The year of the student")
    priority: Priority = Field(default=Priority.low, description="The priority of the student")  