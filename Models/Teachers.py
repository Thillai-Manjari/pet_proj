from typing import Optional
from pydantic import BaseModel

class Teacher(BaseModel):
    Name: str 
    Age: int
    Gender: str
    Department : str
    Blood_Group: str
    Phone_Number: str
    Email_id: str
    Teacher_id: str
    Salary: int
    Designation: str
    Educational_Qualification: str
