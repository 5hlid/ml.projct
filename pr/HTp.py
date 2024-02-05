# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 04:02:10 2024

@author: altul
"""
import numpy as np
import pickle
import streamlit as st
import base64
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()
def set_background(png_file):
    
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_background('C:/Users/mohammed saad/Downloads/2345676.webp')

loaded_model = pickle.load(open("C:/Users/mohammed saad/Downloads/heart.sav",'rb'))


def diabetes1(input_data):
    
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    #return (prediction)
    
    if (prediction[0] == 0):
        return('امورك تمام')
        
    else:
        return('راجع الطبيب')
        
   
    
    

  
def main():
    
    st.title('احتمالية الإصابة بامراض القلب')
    

    Sex_male = st.selectbox('الجنس',    ('ذكر', 'أنثى'))    
    if Sex_male == 'أنثى':
        Sex_male= 0
    else:
        Sex_male = 1 
   
 
    age = st.text_input('العمر : ')
    currentSmoker = st.selectbox('مدخن',    ('نعم', 'لا'))
    if currentSmoker == 'نعم':
       currentSmoker= 0
    else:
       currentSmoker = 1 
    cigsPerDay = st.text_input('معدل عدد السجائر في اليوم : ')
    BPMeds = st.selectbox('هل تستخدم أدوية ضغط',    ('نعم', 'لا'))
    if BPMeds == 'نعم':
       BPMeds= 0
    else:
       BPMeds = 1
    prevalentStroke = st.selectbox('هل سبق ان اصبت بالجلطة ',    ('نعم', 'لا'))
    if prevalentStroke == 'نعم':
       prevalentStroke= 0
    else:
       prevalentStroke = 1 
    prevalentHyp= st.selectbox('هل سبق ان اصبت بتجلط في القلب ',    ('نعم', 'لا'))
    if prevalentHyp == 'نعم':
       prevalentHyp= 0
    else:
       prevalentHyp = 1 
    diabetes = st.selectbox('هل الضغط منخفض ',    ('نعم', 'لا'))
    if diabetes == 'نعم':
       diabetes= 0
    else:
       diabetes = 1 
    totChol= st.number_input('ارتفاع الضغط: ')
    sysBP= st.number_input('السكر: ')
    diaBP   = st.number_input('الكلسترول: ')
    BMI = st.number_input('كتلة الجسم : ')
    heartRate = st.number_input('ضربات القلب : ')
    glucose = st.number_input('الجلكوز : ')
    dignosis = ''
    if st.button('Diabetes test Result'):
        dignosis = diabetes1([Sex_male,age ,currentSmoker,cigsPerDay,BPMeds,prevalentStroke,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,heartRate,glucose])
    st.success(dignosis)
    
if __name__ == '__main__':
    main()

