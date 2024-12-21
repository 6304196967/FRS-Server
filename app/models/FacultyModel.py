from typing import List, Optional
from pydantic import BaseModel
from enum import Enum
from models.StudentModel import Branch , Year , Section  # Ensure Branch is defined correctly

class Faculty(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    password : str
    email_address: str
    phone_number: str
    department: Branch  # Ensure Branch is a valid Pydantic model or Enum
    designation: str
    qualification: str
    subjects: List[str]
    is_admin: bool = False

class FacultyCollection(BaseModel):
    faculties: List[Faculty]  # List of Faculty objects
    
class AttendanceRequest(BaseModel):
    student_id : Optional[str] = None
    branch : Optional[str] = None
    batch : Optional[str] = None
    section : Optional[List[str]] = None

class StudentAttendance(BaseModel):
    id: str
    name: str
    classes_attended: int
    
class Attendance(BaseModel):
    student_id: str
    subject : str
    attended: bool