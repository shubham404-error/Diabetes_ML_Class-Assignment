# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:20:14 2022

@author: ASUS
"""

import pickle as pkl
import streamlit as st

model=pkl.load(open(r"model.sav",'rb'))

def diab_pred(input_data):
    prediction=model.predict(input_data)
    print(prediction)
    if prediction[0]==0:
        return 'Patient is not diabetic'
    else:
        return 'Patient is diabetic'
def main():
    st.title('Diabetes Prediction Web App')
    
    Pregnancies=st.text_input('Enter No of Pregnanices ')
    Glucose=st.text_input('Enter Glucose Level')
    BloodPressure=st.text_input('Enter BloodPressure Level')
    SkinThickness= st.text_input('Enter your SkinThickness Value')
    Insulin= st.text_input('Enter your Insulin level')
    BMI= st.text_input('Enter your BMI Value')
    DiabetesPedigreeFunction= st.text_input('Enter your DiabetesPedigreeFunction')
    Age=st.text_input('Enter your Age')
    
    diagnosis=''
    if st.button('Diabetes Test Result'):
        diagnosis=diab_pred([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        st.success(diagnosis)
