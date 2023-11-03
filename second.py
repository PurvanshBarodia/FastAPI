from fastapi import FastAPI, Path
from pydantic import BaseModel

# creat instance of fastapi
app = FastAPI()



stud ={
    1 :{
        "name":"Purvansh",
        "age":21,
        "year":12
    }
}

# route
@app.get("/")
def index():
    return stud  # json formate

#get, post, put, delete

# we not need to use postman
@app.get("/get-student/{student_id}")
def get_student(student_id:int):
    return stud[student_id]

