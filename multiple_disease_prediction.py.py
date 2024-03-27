import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Get the directory of the current script
current_dir = os.path.dirname(__file__)

# Define file paths relative to the current directory
diabetes_model_path = os.path.join(current_dir, 'mdp', 'diabites_model.sav')
heart_disease_model_path = os.path.join(current_dir, 'mdp', 'heart_model.sav')
kidney_model_path = os.path.join(current_dir, 'mdp', 'kidney_model.sav')

# Load the saved models
diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))
kidney_model = pickle.load(open(kidney_model_path, 'rb'))

# Side bar for navigation
with st.sidebar:
    selected = option_menu('Multiple disease prediction system',
                           ['Diabetes Prediction', 'Heart disease prediction', 'Kidney disease prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes prediction page
if selected == "Diabetes Prediction":
    # Page title
    st.title('Diabetes Prediction using ML')

    # Input fields
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        SkinThickness = st.text_input("Skin Thickness Value")
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    with col2:
        Glucose = st.text_input("Glucose level")
        Insulin = st.text_input("Insulin Level")
        BMI = st.text_input("BMI value")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
        Age = st.text_input("Age of the person")

    # Prediction
    diab_diagnosis = ''
    if st.button("Diabetes Test Results"):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                                                    BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = "The Person is Diabetic"
        else:
            diab_diagnosis = "The Person is Not Diabetic"
    st.success(diab_diagnosis)

# Heart disease prediction
if selected == "Heart disease prediction":
    st.title('Heart disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age of the Person")
        chestpain = st.text_input("Chest Pain Value")
        fastingbloodsugar = st.text_input("Fasting Blood Sugar value")
        restecg = st.text_input("Restecg value")
        exang = st.text_input("Exang value")
        slope = st.text_input("Slope value")
        thal = st.text_input("Thal value")
    with col2:
        sex = st.text_input("Male or Female")
        trestbps = st.text_input("Trestbps Value")
        cholestoral = st.text_input("Cholestoral Level")
        thalach = st.text_input("Thalach value")
        oldpeak = st.text_input("OldPeak value")
        ca = st.text_input("Ca value")

    # Prediction
    heart_diagnosis = ''
    if st.button("Heart Disease Test Results"):
        heart_prediction = heart_disease_model.predict([[age, sex, chestpain, trestbps, cholestoral, fastingbloodsugar,
                                                         restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = "The Person is having heart disease"
        else:
            heart_diagnosis = "The Person is Not having heart disease"
    st.success(heart_diagnosis)

# Kidney disease prediction
if selected == "Kidney disease prediction":
    st.title('Kidney disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        Bp = st.text_input("BP value")
        Al = st.text_input("Al Value")
        Rbc = st.text_input("RBC value")
        Sc = st.text_input("Sc value")
        Pot = st.text_input("Pot value")
        Wbcc = st.text_input("Wbcc value")
    with col2:
        Sg = st.text_input("Sg value")
        Su = st.text_input("SU Value")
        Bu = st.text_input("BU value")
        Sod = st.text_input("Sod value")
        Hemo = st.text_input("Hemo value")
        Rbcc = st.text_input("Rbcc value")
    with col3:
        Htn = st.text_input("Htn value")

    # Prediction
    kidney_diagnosis = ''
    if st.button("Kidney Disease Test Results"):
        kidney_prediction = kidney_model.predict([[Bp, Sg, Al, Su, Rbc, Bu, Sc, Sod, Pot, Hemo, Wbcc, Rbcc, Htn]])

        if kidney_prediction[0] == 1:
            kidney_diagnosis = "The Person is having kidney disease"
        else:
            kidney_diagnosis = "The Person is Not having kidney disease"
    st.success(kidney_diagnosis)
