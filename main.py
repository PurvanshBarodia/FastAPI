from fastapi import FastAPI
from enum import Enum
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    name:str
    description:Union[str,None] = None
    price:float
    tax : Union[float,None] = None

# operation path decorators
@app.get("/")
def root():
    return {"message":"Hello World"}

# you can return dict,int,float,string... pydantic datatypes

# path parameters

@app.get("/items/{item_id}")
def read_item(item_id:int):
    return item_id


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.post("/create-items/")
def create_item(item:Item):
    return item

