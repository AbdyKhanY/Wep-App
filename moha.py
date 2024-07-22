# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:16:52 2024

@author: USER
"""

import numpy as np
import pickle
import streamlit as st
import os
import requests

# Check for scikit-learn installation
try:
    import sklearn
    st.write(f"Scikit-learn version: {sklearn.__version__}")
except ImportError:
    st.error("Scikit-learn is not installed. Please check your requirements.txt file.")

# Function to download files from GitHub
def download_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
        st.write(f"Downloaded {filename} successfully")
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to download {filename} from {url}: {e}")

# URLs of the model files on GitHub
parkinsons_model_url = "https://github.com/AbdyKhanY/Mohaa/blob/4672d5b9b4cf79de5111edd89cab79590c5719b5/parkinsons_model.pkl"

# Download model files if they do not exist
if not os.path.exists('parkinsons_model.pkl'):
    st.write("Downloading model file...")
    download_file(parkinsons_model_url, 'parkinsons_model.pkl')

# Check if model files exist and load them
try:
    if os.path.exists('parkinsons_model.pkl'):
        st.write("Loading model file...")
        with open('parkinsons_model.pkl', 'rb') as file:
            parkinsons_model = pickle.load(file)
        st.write("Model loaded successfully")
    else:
        st.error("parkinsons_model.pkl not found")
except Exception as e:
    st.error(f"Error loading model files: {e}")

# Creating a function for prediction
def parkinsons_disease_prediction(input_data):
    st.write("Predicting...")
    st.write(f"Input data: {input_data}")

    # Change the input data into numpy array
    try:
        input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    except ValueError as e:
        st.error(f"Error converting input data to numpy array: {e}")
        return None

    st.write(f"Input data as numpy array: {input_data_as_numpy_array}")

    # Reshape the numpy array as we are predicting for only one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    st.write(f"Input data reshaped: {input_data_reshaped}")

    try:
        prediction = parkinsons_model.predict(input_data_reshaped)
        st.write(f"Prediction: {prediction}")
    except Exception as e:
        st.error(f"Error during model prediction: {e}")
        return None

    if prediction[0] == 0:
        return 'The Person does not have Parkinson\'s Disease'
    else:
        return 'The Person has Parkinson\'s Disease'

def main():
    # Giving title for our webpage
    st.title('Parkinson\'s Disease Prediction Web App')

    # Getting input data from user
    inputs = {}
    inputs['MDVP_Fo_Hz'] = st.text_input('MDVP_Fo(Hz)')
    inputs['MDVP_Fhi_Hz'] = st.text_input('MDVP_Fhi(Hz)')
    inputs['MDVP_Flo_Hz'] = st.text_input('MDVP_Flo(Hz)')
    inputs['MDVP_Jitter_percent'] = st.text_input('MDVP_Jitter(%)')
    inputs['MDVP_Jitter_Abs'] = st.text_input('MDVP_Jitter(Abs)')
    inputs['MDVP_RAP'] = st.text_input('MDVP_RAP')
    inputs['MDVP_PPQ'] = st.text_input('MDVP_PPQ')
    inputs['Jitter_DDP'] = st.text_input('Jitter_DDP')
    inputs['MDVP_Shimmer'] = st.text_input('MDVP_Shimmer')
    inputs['MDVP_Shimmer_dB'] = st.text_input('MDVP_Shimmer(dB)')
    inputs['Shimmer_APQ3'] = st.text_input('Shimmer_APQ3')
    inputs['Shimmer_APQ5'] = st.text_input('Shimmer_APQ5')
    inputs['MDVP_APQ'] = st.text_input('MDVP_APQ')
    inputs['Shimmer_DDA'] = st.text_input('Shimmer_DDA')
    inputs['NHR'] = st.text_input('NHR')
    inputs['HNR'] = st.text_input('HNR')
    inputs['RPDE'] = st.text_input('RPDE')
    inputs['DFA'] = st.text_input('DFA')
    inputs['spread1'] = st.text_input('spread1')
    inputs['spread2'] = st.text_input('spread2')
    inputs['D2'] = st.text_input('D2')
    inputs['PPE'] = st.text_input('PPE')

    # Creating a button for prediction
    if st.button('Parkinson\'s Disease Test Result'):
        try:
            input_data = [inputs[key] for key in inputs]
            st.write(f"Collected input data: {input_data}")
            diagnosis = parkinsons_disease_prediction(input_data)
            if diagnosis:
                st.success(diagnosis)
        except ValueError as e:
            st.error(f"Please enter valid numeric values: {e}")

if __name__ == '__main__':
    main()
