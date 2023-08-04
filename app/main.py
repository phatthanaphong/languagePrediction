from fastapi import FastAPI
import pickle
import re
import os
from app.code import predict_language


app = FastAPI()

m = pickle.load(open(os.getcwd()+'/model/cls_langauage_0.1.pkl', 'rb'))
cv = pickle.load(open(os.getcwd()+'/model/cv_feature.pkl', 'rb'))

@app.get("/")
def root():
    return {"message": "This is my api"}


@app.get("/api/predict{item_str}")
def read_str(item_str):
    lang = predict_language(m, cv, item_str)
    return {"language": lang}
