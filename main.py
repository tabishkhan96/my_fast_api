import  uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,Text
from datetime import datetime

app = FastAPI()

student_db = []


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",  port=8000)




                                                               # post model
class Student(BaseModel):

    name:str
    age:int
    course:str
    content:Text

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age:  Optional[int] = None
    course: Optional[str] = None
    content: Optional[Text] = None

    # read_post
@app.get("/")
def index():
    return {"Home":"HomePage"}


                                                                  # add_post
@app.post("/add-student/{id}")
def add_student(id: int, student: Student):
    student_db.append(student)
    return student





                                                                   # get_post
@app.get("/get-student/{id}")
def get_student():
    return student_db



                                                                   # update_post
@app.put("/update-student/{id}")
def update_student(id: int, student: UpdateStudent):

    result = {"id":id, **student.dict()}

    return result


                                                                   # delete_post
@app.delete("/delete-student/{id}")
def delete_student(id: int):

    if id not in student_db:
        return {"Error":"student does not exist"}

    del student_db[id]
    return {"Message":"student deleted successfully"}



