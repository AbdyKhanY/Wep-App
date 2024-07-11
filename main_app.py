# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:07:32 2024

@author: MR KHAN
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 09:07:32 2024

@author: MR KHAN
"""
# Import basic libraries
import numpy as np
import pickle
import streamlit as st

# Loading the saved models
heart_disease_model = pickle.load(open('heart_disease_model.pkl', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.pkl', 'rb'))

# Creating functions for predictions
def heart_disease_prediction(input_data):
    # Change the input data into numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)

    # Reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = heart_disease_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'The Person does not have a Heart Disease'
    else:
        return 'The Person has Heart Disease'

def parkinsons_disease_prediction(input_data):
    # Change the input data into numpy array
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)

    # Reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = parkinsons_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return 'Parkinsons Negative'
    else:
        return 'Parkinsons Positive'

def main():
    # Sidebar for navigation
    st.sidebar.title("PREDICTIONS")
    selection = st.sidebar.radio("Go to", ["Heart Disease Prediction", "Parkinsons Disease Prediction"])

    if selection == "Heart Disease Prediction":
        # Heart Disease Prediction Page
        st.title('HEART DISEASE PREDICTION APP')
        st.image("C:/Users/Windows 10 Pro/Desktop/Machine learning/Heart Disease/heart.jpg")

        # Getting input data from user
        age = st.text_input('Age of the Person')
        sex = st.selectbox('Gender', options=['Male', 'Female'])
        cp = st.selectbox('Chest pain type', options=['0: Typical angina', '1: Atypical angina', '2: Non-anginal pain', '3: Asymptomatic'])
        trestbps = st.text_input('Resting Blood Pressure')
        chol = st.text_input('Serum Cholesterol in mg/dl')
        fbs = st.selectbox('Fasting blood Sugar > 120 mg/dl', options=['Yes', 'No'])
        restecg = st.selectbox('Resting Electrocardiographic Results', options=['0: Normal', '1: Having ST-T wave abnormality', '2: Showing probable or definite left ventricular hypertrophy'])
        thalach = st.text_input('Maximum Heart Rate Achieved')
        exang = st.selectbox('Exercise Induced Angina', options=['Yes', 'No'])
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
        slope = st.selectbox('Slope of the peak exercise ST segment', options=['0: Upsloping', '1: Flat', '2: Downsloping'])
        ca = st.selectbox('Number of Major Vessels colored by fluoroscopy', options=['0', '1', '2', '3'])
        thal = st.selectbox('Thal', options=['0: Normal', '1: Fixed Defect', '2: Reversable Defect'])

        # Map input selections to numerical values
        sex = 1 if sex == 'Male' else 0
        fbs = 1 if fbs == 'Yes' else 0
        exang = 1 if exang == 'Yes' else 0
        cp = int(cp.split(':')[0])
        restecg = int(restecg.split(':')[0])
        slope = int(slope.split(':')[0])
        thal = int(thal.split(':')[0])

        # Code for prediction
        diagnosis = ''

        # Creating a button for prediction
        if st.button('Heart Disease Test Result'):
            try:
                diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
                st.success(diagnosis)
            except ValueError:
                st.error("Please enter valid numeric values.")

    elif selection == "Parkinsons Disease Prediction":
        # Parkinsons Disease Prediction Page
        st.title('PARKINSONS PREDICTION APP')
        st.image("C:/Users/Windows 10 Pro/Desktop/Machine learning/Parkinson Disease/PARKINSONS.jpeg")

        # Getting input data from user
        MDVP_Fo_Hz = st.text_input('MDVP:Fo(Hz)')
        MDVP_Fhi_Hz = st.text_input('MDVP:Fhi(Hz)')
        MDVP_Flo_Hz = st.text_input('MDVP:Flo(Hz)')
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        MDVP_RAP = st.text_input('MDVP:RAP')
        MDVP_PPQ = st.text_input('MDVP:PPQ')
        Jitter_DDP = st.text_input('Jitter:DDP')
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
        MDVP_APQ = st.text_input('MDVP:APQ')
        Shimmer_DDA = st.text_input('Shimmer:DDA')
        NHR = st.text_input('NHR')
        HNR = st.text_input('HNR')
        RPDE = st.text_input('RPDE')
        DFA = st.text_input('DFA')
        spread1 = st.text_input('spread1')
        spread2 = st.text_input('spread2')
        D2 = st.text_input('D2')
        PPE = st.text_input('PPE')

        # Code for prediction
        diagnosis = ''

        # Creating a button for prediction
        if st.button('Parkinsons Disease Test Result'):
            try:
                diagnosis = parkinsons_disease_prediction([MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE])
                st.success(diagnosis)
            except ValueError:
                st.error("Please enter valid numeric values.")

if __name__ == '__main__':
    main()
