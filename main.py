from enum import IntEnum
from fastapi import FastAPI, Path, HTTPException
from typing import Optional, List
from pydantic import BaseModel, Field

api = FastAPI()

class Priority(IntEnum):
    low = 1
    medium = 2
    high = 3

class StudentBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="The name of the student")
    age: int  = Field(..., gt=0, le=120, description="The age of the student")
    year: str = Field(..., min_length=2, max_length=50, description="The year of the student")
    priority: Priority = Field(default=Priority.low, description="The priority of the student")  
    

class CreateStudent(StudentBase):
    pass

class UpdateStudent(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50, description="The name of the student")
    age: Optional[int]  = Field(None, gt=0, le=120, description="The age of the student")
    priority: Optional[Priority] = Field(None, description="The priority of the student")    

class Student(StudentBase):
    person_id: int = Field(..., description="Unique identifier of the student")


students = [
    Student(person_id =1, name="John", age=20, year="Year 12", priority=Priority.low), 
    Student(person_id =2, name="Marco", age=35, year="Year 09", priority=Priority.high)
]

#GET, POST, PUT, DELETE
@api.get("/")
def index():
    return {"message": "Hello World"}

@api.get("/students", response_model=List[Student]) # response_model is used to specify the response model
def get_student():
    return students

@api.get("/students/{student_id}", response_model=Student) # response_model is used to specify the response model
def get_student_by_id(student_id: int = Path(..., description="The ID of the student to get", gt=0)): #... it means the data is required
    for student in students:
        if student.person_id == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@api.get("/by-name/{student_id}", response_model=Student)
def get_student_by_query(*, name: Optional[str] = None, student_id: int):
    if name is None:
        raise HTTPException(status_code=404, detail="Name not provided")
    
    for student in students:
        if student.person_id == student_id and student.name.lower() == name.lower():
            return student
    raise HTTPException(status_code=404, detail="Student not found")

@api.post("/create-student/")
def create_student_by_id(student: CreateStudent, response_model=Student):
    student_found = next((item for item in students if student.name == item.name), None)
    if student_found is not None:
        raise HTTPException(status_code=404, detail="Student already exists")
    
    person_id = max(student.person_id for student in students) + 1
    
    new_student = Student(person_id = person_id, name = student.name, age = student.age, year = student.year, priority = student.priority)
    students.append(new_student)
    return new_student

@api.put("/update-student/{student_id}", response_model=Student)
def update_student_by_id(student_id: int, student: UpdateStudent):
    student_found = next((item for item in students if student_id == item.person_id), None)
    if student_found is None:
        raise HTTPException(status_code=404, detail="Student not found")
        
    if student.name != None:
        student_found.name = student.name
        
    if student.age != None:
        student_found.age = student.age
        
    if student.priority != None:
        student_found.priority = student.priority
        
    return student_found

@api.delete("/delete-student/{student_id}", response_model=Student)
def delete_student_by_id(student_id: int):
    for index, student in enumerate(students):
        if student.person_id == student_id:
            deleted_student = students.pop(index)
            return deleted_student
    
    raise HTTPException(status_code=404, detail="Student not found")

@api.get("/getdata")
async def get_data_from_db():
    # Simulate a database call
    data = await simulate_db_call()
    return {"data": data}

async def simulate_db_call():
    pass
    return ""