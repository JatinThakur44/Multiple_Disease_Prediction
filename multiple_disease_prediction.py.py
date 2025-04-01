import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define file paths correctly
diabetes_model_path = os.path.join(current_dir, 'mdp', 'diabites_model.sav')
heart_disease_model_path = os.path.join(current_dir, 'mdp', 'heart_model.sav')
kidney_model_path = os.path.join(current_dir, 'mdp', 'kidney_model.sav')

# Load models if they exist
if os.path.exists(diabetes_model_path):
    diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
else:
    st.error(f"Model file not found: {diabetes_model_path}")

if os.path.exists(heart_disease_model_path):
    heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))
else:
    st.error(f"Model file not found: {heart_disease_model_path}")

if os.path.exists(kidney_model_path):
    kidney_model = pickle.load(open(kidney_model_path, 'rb'))
else:
    st.error(f"Model file not found: {kidney_model_path}")

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Kidney Disease Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title('Diabetes Prediction using ML')
    
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

    if st.button("Diabetes Test Results"):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                                                    BMI, DiabetesPedigreeFunction, Age]])
        st.success("The person is Diabetic" if diab_prediction[0] == 1 else "The person is Not Diabetic")

# Heart Disease Prediction Page
if selected == "Heart Disease Prediction":
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input("Age")
        chestpain = st.text_input("Chest Pain Type")
        fastingbloodsugar = st.text_input("Fasting Blood Sugar > 120 mg/dl")
        restecg = st.text_input("Resting ECG Result")
        exang = st.text_input("Exercise Induced Angina")
        slope = st.text_input("Slope Value")
        thal = st.text_input("Thalassemia Value")
    with col2:
        sex = st.text_input("Sex (0 = Female, 1 = Male)")
        trestbps = st.text_input("Resting Blood Pressure")
        cholestoral = st.text_input("Serum Cholesterol")
        thalach = st.text_input("Maximum Heart Rate")
        oldpeak = st.text_input("ST Depression Induced by Exercise")
        ca = st.text_input("Number of Major Vessels Colored by Fluoroscopy")
    
    if st.button("Heart Disease Test Results"):
        heart_prediction = heart_disease_model.predict([[age, sex, chestpain, trestbps, cholestoral, fastingbloodsugar,
                                                         restecg, thalach, exang, oldpeak, slope, ca, thal]])
        st.success("The person has heart disease" if heart_prediction[0] == 1 else "The person does not have heart disease")

# Kidney Disease Prediction Page
if selected == "Kidney Disease Prediction":
    st.title('Kidney Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    with col1:
        Bp = st.text_input("Blood Pressure")
        Al = st.text_input("Albumin")
        Rbc = st.text_input("Red Blood Cells")
        Sc = st.text_input("Serum Creatinine")
        Pot = st.text_input("Potassium Level")
        Wbcc = st.text_input("White Blood Cell Count")
    with col2:
        Sg = st.text_input("Specific Gravity")
        Su = st.text_input("Sugar")
        Bu = st.text_input("Blood Urea")
        Sod = st.text_input("Sodium Level")
        Hemo = st.text_input("Hemoglobin Level")
        Rbcc = st.text_input("Red Blood Cell Count")
    with col3:
        Htn = st.text_input("Hypertension (0 = No, 1 = Yes)")

    if st.button("Kidney Disease Test Results"):
        kidney_prediction = kidney_model.predict([[Bp, Sg, Al, Su, Rbc, Bu, Sc, Sod, Pot, Hemo, Wbcc, Rbcc, Htn]])
        st.success("The person has kidney disease" if kidney_prediction[0] == 1 else "The person does not have kidney disease")
