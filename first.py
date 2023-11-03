from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional

# creat instance of fastapi
app = FastAPI()



stud ={
    1 :{
        "name":"Purvansh",
        "age":21,
        "year":12
    }
}

class Students(BaseModel):
    name:str
    age:int
    year:int

class UpdateStud (BaseModel):
    name: Optional[str]=None
    age: Optional[int]= None
    year: Optional[int] = None

# route
@app.get("/")
def index():
    return stud  # json formate

#get, post, put, delete
# get : get an information
# post : create something new
# put : update existing
# delete : delete something

# we not need to use postman
@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return stud[student_id]


# query perameter
@app.get("/get-by-name")
def get_student(std_name: str):
    for student_id in stud:
        student = stud.get(student_id)
        if student and student.get("name") == std_name:
            return student
    return {'Data': "Not Found"}

#to create something new 
@app.post("/create-student/{student_id}")
def create_student(student_id:int,student:Students):
    if student_id in stud:
        return {"Error":"Data Already Exits."}
    else:
        stud[student_id] = student.dict()
    return stud[student_id]

@app.put("/update-student/{student_id}")
# Here, student is object of UpdateStud
# if we want to use student["name"] instead of student.name
# convert pydantic data type to dict (using student = student.dict())

def update_student(student_id:int,student:UpdateStud):
    if student_id not in stud:
        return {"Error":"Student does not exits."}
    if student.name!=None:
        stud[student_id]["name"] = student.name
    if student.age!=None:
        stud[student_id]["age"] = student.age
    if student.year!=None:
        stud[student_id]["year"] = student.year

    return stud[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id not in stud:
        return {"Error":"Student does not exits."}
    else:
        del stud[student_id]
        return {"Message":"Student deleted successfully."}
