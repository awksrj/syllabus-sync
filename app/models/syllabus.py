from pydantic import BaseModel
from typing import List, Optional

class Assignment(BaseModel):
    title: str
    due_date: str
    points: Optional[int]

class Syllabus(BaseModel):
    course_name: str
    instructor: str
    contact_email: str
    grading_breakdown: dict
    meeting_times: str
    assignments: List[Assignment]
