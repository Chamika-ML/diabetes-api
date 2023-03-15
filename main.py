# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 13:22:09 2023

@author: Anuruddha
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# app gives the permision to access any user by indicating *
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# user inputs
class model_input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
       

# load the model
diabetes_model = pickle.load(open('trainned_model.sav', 'rb'))

@app.post('/diabetes_prediction') # end point for user

# predcting function 
def diabetes_predd(input_parameters : model_input):
    
    input_data = input_parameters.json() # input data --> json data
    input_dictionary = json.loads(input_data) # json data --> dictionary
    
    # make user input data list
    preg = input_dictionary["Pregnancies"]
    glu = input_dictionary["Glucose"]     
    bp = input_dictionary["BloodPressure"]     
    skin = input_dictionary["SkinThickness"]     
    insulin = input_dictionary["Insulin"]     
    bmi = input_dictionary["BMI"]     
    dpf = input_dictionary["DiabetesPedigreeFunction"]     
    age = input_dictionary["Age"]     
    
    input_list = [preg,glu,bp,skin,insulin,bmi,dpf,age] 
    
    # prediction
    prediction = diabetes_model.predict([input_list]) 
    
    if prediction[0]==0:
        return "The person is not Diabetes"
    else:
        return "The person is Diabetes"
    