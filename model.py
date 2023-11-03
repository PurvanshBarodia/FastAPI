import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import sklearn

# unserialize pickle model
pickle_in = open("model.pkl",'rb')
classifier = pickle.load(pickle_in)

# create instance of FastAPI
app = FastAPI()

# create class for request body
class BankNote(BaseModel):
    variance : float
    skewness : float
    curtosis : float
    entropy : float

@app.post("/predict")
def predict_banknote(data:BankNote):
    data = data.dict()
    variance = data['variance']
    skewness =  data['skewness']
    curtosis =  data['curtosis']
    entropy =  data['entropy']

    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])

    if prediction[0] == 0:
        return {"Prediction":"It is Valid Bank Note."}
    else:
        return {"Prediction":"Fake Note."}

