from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: str
    gender: str
    department: str
    credit_score: str
    blood_group: str
    email: str
    roll_no: str
    year: str