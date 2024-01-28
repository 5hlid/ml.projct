# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 04:02:10 2024

@author: altul
"""

import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# function 
def diabetes (input_data):
    #input_data = (5,166,72,19,175,25.8,0.587,51)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)


    if (prediction[0] == 0):
      return('The person is not diabetic')
    else:
      return('The person is diabetic')
    return (prediction)
    
def main():
    
      
      # the name of the websit
    st.title('Diabetes Prediction Web App')
    
    Pregnancies = st.number_input('Enter the number of pregnancies: ',step=1,placeholder="insert num")
    Glucose = st.number_input('Enter the glucose level: ',step=1,placeholder="insert num")
    BloodPressure = st.number_input('Enter the blood pressure: ',step=1,placeholder="insert num")
    SkinThickness = st.number_input('Enter the skin thickness: ',step=1,placeholder="insert num")
    Insulin = st.number_input('Enter the insulin level: ',step=1,placeholder="insert num")
    BMI = st.number_input('Enter the BMI: ',step=1,placeholder="insert num")
    DiabetesPedigreeFunction = st.number_input('Enter the diabetes pedigree function: ',step=1,placeholder="insert num")
    Age = st.number_input('Enter the age: ',step=1,placeholder="insert num")
    
    
    # code for pediction 
    dignosis = ''
    # creating a button for perdiction
    if st.button('Diabetes test Result'):
        dignosis = diabetes([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        
    st.success(dignosis)
    
if __name__ == '__main__':
    main()