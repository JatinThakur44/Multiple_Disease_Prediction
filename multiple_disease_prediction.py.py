# -*- coding: utf-8 -*-
"""
Created on Tue May 16 00:36:03 2023

@author: jatin
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(
    open('C:/Users/jatin/PycharmProjects/Multiple Disease Prediction/mdp/diabites_model.sav', 'rb'))

heart_disease_model = pickle.load(
    open('C:/Users/jatin/PycharmProjects/Multiple Disease Prediction/mdp/heart_model.sav', 'rb'))

kidney_model = pickle.load(
    open('C:/Users/jatin/PycharmProjects/Multiple Disease Prediction/mdp/kidney_model.sav', 'rb'))

# side barr for navigation
with st.sidebar:
    selected = option_menu('Multiple disease prediction system',

                           ['Diabetes Prediction',
                            'Heart disease prediction',
                            'Kidney disease prediction'],

                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# diabetes prediction page
if selected == "Diabetes Prediction":
    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    # columns for the input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
    with col2:
        Glucose = st.text_input("Glucose level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    with col2:
        Age = st.text_input("Age of the person")

    # code for prediction
    diab_diagnosis = ''
    # creating a button for prediction
    if st.button("Diabetes Test Results"):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = "The Person is Diabetic"
        else:
            diab_diagnosis = "The Person is Not Diabetic"
    st.success(diab_diagnosis)

if selected == "Heart disease prediction":

    st.title('Heart disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age of the Person")
    with col2:
        sex = st.text_input("Male or Female")
    with col3:
        chestpain = st.text_input("Chest Pain Value")
    with col1:
        trestbps = st.text_input("Trestbps Value")
    with col2:
        cholestoral = st.text_input("Cholestoral Level")
    with col3:
        fastingbloodsugar = st.text_input("Fasting Blood Sugar value")
    with col1:
        restecg = st.text_input("Restecg value")
    with col2:
        thalach = st.text_input("Thalach value")
    with col3:
        exang = st.text_input("Exang value")
    with col1:
        oldpeak = st.text_input("OldPeak value")
    with col2:
        slope = st.text_input("Slope value")
    with col3:
        ca = st.text_input("Ca value")
    with col1:
        thal = st.text_input("Thal value")

    # code for prediction
    heart_diagnosis = ''
    # creating a button for prediction
    if st.button("Heart Disease Test Results"):
        heart_prediction = heart_disease_model.predict([[age, sex, chestpain, trestbps, cholestoral, fastingbloodsugar,
                                                         restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = "The Person is having heart disease"
        else:
            heart_diagnosis = "The Person is Not having heart disease"
    st.success(heart_diagnosis)

if selected == "Kidney disease prediction":
    st.title('Kidney disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Bp = st.text_input("BP value")
    with col2:
        Sg = st.text_input("Sg value")
    with col3:
        Al = st.text_input("Al Value")
    with col1:
        Su = st.text_input("SU Value")
    with col2:
        Rbc = st.text_input("RBC value")
    with col3:
        Bu = st.text_input("BU value")
    with col1:
        Sc = st.text_input("Sc value")
    with col2:
        Sod = st.text_input("Sod value")
    with col3:
        Pot = st.text_input("Pot value")
    with col1:
        Hemo = st.text_input("Hemo value")
    with col2:
        Wbcc = st.text_input("Wbcc value")
    with col3:
        Rbcc = st.text_input("Rbcc value")
    with col1:
        Htn = st.text_input("Htn value")

    # code for prediction
    kidney_diagnosis = ''
    # creating a button for prediction
    if st.button("Kidney Disease Test Results"):
        kidney_prediction = kidney_model.predict([[Bp, Sg, Al, Su, Rbc, Bu, Sc, Sod, Pot, Hemo, Wbcc, Rbcc, Htn]])

        if kidney_prediction[0] == 1:
            kidney_diagnosis = "The Person is having kidney disease"
        else:
            kidney_diagnosis = "The Person is Not having kidney disease"
    st.success(kidney_diagnosis)
